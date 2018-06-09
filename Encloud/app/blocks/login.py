from django.template import loader
from django.http import HttpResponse
from app.forms import *
from app.models import *
import pdb
import datetime
from django.shortcuts import redirect
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.core.mail import send_mail
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from app.Mailing.draft import *

def login_request(request):
    context, perm_list = {}, {}
    if str(request.user)!='AnonymousUser':
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                context['failure'] = True
                context['message'] = "Invalid Username/Password"
                template = loader.get_template('app/mydir/login.html')

            return HttpResponse(template.render(context, request))
    template = loader.get_template('app/mydir/login.html')
    return HttpResponse(template.render(context, request))


def lostpassword(request):
    context={}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        phoneno = request.POST.get('phoneno', '')
        email = request.POST.get('emailid', '')
        q = Profile.objects.filter(phoneno=phoneno) | Profile.objects.filter(user__email=email) | Profile.objects.filter(user__username=username)
        context['results'] = q
    template = loader.get_template('app/mydir/lostpassword.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='login.html')
def logout_request(request):
    logout(request)
    template = loader.get_template('app/mydir/login.html')
    return HttpResponse(template.render({}, request))


@login_required(login_url='login.html')
def resetpassword(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.method == 'POST':
        oldpassword = request.POST.get('oldpassword', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if request.user.check_password(oldpassword):
            user = request.user
            user.set_password(password)
            user.save()
            context['success'] = 1
            context['message'] = "Password changed successfully. Log in once again to continue."
        else:
            context['failure'] = 1
            context['message'] = "Password change failed"
    template = loader.get_template('app/mydir/resetpassword.html')
    return HttpResponse(template.render(context, request))


def mailpassword(request):
    data = {}
    if request.GET['username']:
        u = User.objects.get(username=request.GET['username'])
        password = User.objects.make_random_password(length=6)
        u.set_password(password)
        u.save()
        kwargs = {'fail_silently': False, 'html_message': My_HTML_Mail_reset(Profile.objects.filter(user=u)[0].name, u.username, password),
                  'recipient_list': [u.email],
                  'from_email': 'care@clubayurveda.com', 'message': '', 'subject': 'Reset your password'}
        send_mail(**kwargs)
        data = {'success': 1}
    return JsonResponse(data)

@login_required(login_url='login.html')
def editprofile(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.method == 'POST':
            # CHANGE COMPANY LOGO
            myfile = request.FILES['logo']
            fs = FileSystemStorage('app/static/images')
            if fs.exists("logo.png"):
                fs.delete("logo.png")
            fs.save("logo.png", myfile)
    template = loader.get_template('app/mydir/editprofile.html')
    return HttpResponse(template.render(context, request))
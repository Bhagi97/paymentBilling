from django.template import loader
from django.http import HttpResponse
import pdb
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.signals import user_logged_in
from app.blocks.helper import *
from django.shortcuts import redirect

# To template different kind of users
def permission_templates(code):
    mydict = '''{   'Accounts': {   "fr_a": false,'fr_d': false,'fr_e': false,
                                    'im_c': false,'im_pa': false,'im_pr': false,'im_sa': false,
                                    'im_se': false,'im_sku': false,'im_st': false,'im_tr': false,
                                    'perm1': false,'perm2': false,'perm3': false,'perm4': false,
                                    'permb1': false,'permb2': false,'permb6': false,
                                    'permd1': false,'permd2': false,'permd3': false,'permd4': false,
                                    'permd5': false,'permd6': false,'permd7': false,
                                    'permdis1': false,'permdis2': false,
                                    'permr1': true,'permr2': true,'permr3': true,'permr5': true,'permr6': true,'permr7': false,
                                    'permu1': false,'permu2': false},
                    'Admin': {   'fr_a': true,'fr_d': true,'fr_e': true,
                                 'im_c': true,'im_pa': true,'im_pr': true,'im_sa': true,'im_se': true,'im_sku': true,'im_st': true,'im_tr': true,
                                 'perm1': true,'perm2': true,'perm3': true,'perm4': true,
                                 'permb1': true,'permb2': true,'permb6': true,
                                 'permd1': true,'permd2': true,'permd3': true,'permd4': true,'permd5': true,'permd6': true,'permd7': true,
                                 'permdis1': true,'permdis2': true,
                                 'permr1': true,'permr2': true,'permr3': true,'permr5': true,'permr6': true,'permr7': true,
                                 'permu1': true,'permu2': true	},
                    'Vendor': {    'fr_a': false,'fr_d': false,'fr_e': false,
                                        'im_c': false,'im_pa': false,'im_pr': false,'im_sa': false,'im_se': false,'im_sku': false,'im_st': false,'im_tr': false,
                                        'perm1': false,'perm2': false,'perm3': false,'perm4': false,
                                        'permb1': false,'permb2': false,'permb6': false,
                                        'permd1': false,'permd2': false,'permd3': false,'permd4': false,'permd5': false,'permd6': false,'permd7': false,
                                        'permdis1': true,'permdis2': true,
                                        'permr1': true,'permr2': true,'permr3': true,'permr5': true,'permr6': true,'permr7': false,
                                        'permu1': false,'permu2': false	},
                    'Doctor': {   'fr_a': false, 'fr_d': false, 'fr_e': false,
                                  'im_c': false, 'im_pa': false, 'im_pr': false, 'im_sa': false, 'im_se': false, 'im_sku': false, 'im_st': false, 'im_tr': false, 
                                  'perm1': false, 'perm2': false, 'perm3': false, 'perm4': false, 
                                  'permb1': false, 'permb2': false,'permb6': false, 
                                  'permd1': false, 'permd2': true, 'permd3': true, 'permd4': false, 'permd5': false, 'permd6': false, 'permd7': true, 
                                  'permdis1': false, 'permdis2': false, 
                                  'permr1': false, 'permr2': false, 'permr3': false, 'permr5': false, 'permr6': false, 'permr7': true, 
                                  'permu1': false, 'permu2': false	},
                    'Pharmacist': {   'fr_a': false,'fr_d': false,'fr_e': false,
                                      'im_c': false,'im_pa': false,'im_pr': false,'im_sa': false,'im_se': false,'im_sku': false,'im_st': false,'im_tr': false,
                                      'perm1': false,'perm2': false,'perm3': false,'perm4': false,
                                      'permb1': true,'permb2': true,'permb6': false,
                                      'permd1': false,'permd2': false,'permd3': false,'permd4': false,'permd5': false,'permd6': false,'permd7': false,
                                      'permdis1': false,'permdis2': false,
                                      'permr1': false,'permr2': false,'permr3': true,'permr5': false,'permr6': false,'permr7': true,
                                      'permu1': false,'permu2': false	},
                    'Receptionist': {   'fr_a': false, 'fr_d': false, 'fr_e': false, 
                                        'im_c': false, 'im_pa': false, 'im_pr': false, 'im_sa': false, 'im_se': false, 'im_sku': false, 'im_st': false, 'im_tr': false, 
                                        'perm1': false, 'perm2': false, 'perm3': false, 'perm4': false, 
                                        'permb1': false, 'permb2': false,'permb6': false, 
                                        'permd1': true, 'permd2': false, 'permd3': false, 'permd4': false, 'permd5': true, 'permd6': true, 'permd7': false, 
                                        'permdis1': false, 'permdis2': false, 
                                        'permr1': false, 'permr2': false, 'permr3': false, 'permr5': false, 'permr6': false, 'permr7': false, 
                                        'permu1': false, 'permu2': false	}}'''
    return mydict



@permission_required('app.adduser', login_url='/page_403.html')
def adduser(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['notify']=0
    if request.method == 'POST':
        name = request.POST.get('name', '')
        username = request.POST.get('username', '')
        emailid = request.POST.get('emailid', '')
        password = User.objects.make_random_password(length=6)
        organisation = request.POST.get('organisation','')
        regid = request.POST.get('regid','0')
        if organisation == '':
            organisation = Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0].franchise_name
        role = request.POST.get('role','')
        phoneno = request.POST.get('phoneno','')
        user = User.objects.create_user(username, emailid, password)
        user.save()
        if role=='Vendor':
            organisation = 'Main Office'
            user.user_permissions.add(Permission.objects.get(codename='vendor'))
        if organisation!="Main Office":
            franchise_code = Franchise.objects.filter(franchise_name=organisation).get().id
        else:
            franchise_code = 0 #-- 0 SYMBOLISES MAIN OFFICE
        kwargs = {'user':user, 'name':name, 'role':role, 'organisation':organisation, 'franchise_code':franchise_code, 'regid':regid, 'phoneno':phoneno }
        profile = Profile(**kwargs)
        profile.save()
        if request.POST.get('fr_a', '') == 'on':
            user.user_permissions.add(Permission.objects.get(codename='add_franchise'))
        user.user_permissions.add(Permission.objects.get(codename='change_franchise')) if request.POST.get('fr_d', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='delete_franchise')) if request.POST.get('fr_e', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Category'), Permission.objects.get(codename='change_Category'), Permission.objects.get(codename='delete_Category')) if request.POST.get('im_c', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_SKUList'), Permission.objects.get(codename='change_SKUList'), Permission.objects.get(codename='delete_SKUList')) if request.POST.get('im_sku', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Product'), Permission.objects.get(codename='change_Product'), Permission.objects.get(codename='delete_Product')) if request.POST.get('im_pr', '') == 'on' else nop()
        if franchise_code == 0:
            user.user_permissions.add(Permission.objects.get(codename='add_Package'), Permission.objects.get(codename='change_Package'), Permission.objects.get(codename='delete_Package')) if request.POST.get('im_pa', '') == 'on' else nop()
            user.user_permissions.add(Permission.objects.get(codename='add_Service'), Permission.objects.get(codename='change_Service'), Permission.objects.get(codename='delete_Service')) if request.POST.get('im_pa', '') == 'on' else nop()
        else:
            user.user_permissions.add(Permission.objects.get(codename='add_PackageMask'), Permission.objects.get(codename='change_PackageMask'), Permission.objects.get(codename='delete_PackageMask')) if request.POST.get('im_pa', '') == 'on' else nop()
            user.user_permissions.add(Permission.objects.get(codename='add_ServiceMask'), Permission.objects.get(codename='change_ServiceMask'), Permission.objects.get(codename='delete_ServiceMask')) if request.POST.get('im_pa', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Stock'), Permission.objects.get(codename='change_Stock'), Permission.objects.get(codename='delete_Stock')) if request.POST.get('im_sa', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_StockTransfer'), Permission.objects.get(codename='change_StockTransfer'), Permission.objects.get(codename='delete_StockTransfer')) if request.POST.get('im_st', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='itemwise_discount')) if request.POST.get('perm1', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='categorywise_discount')) if request.POST.get('perm2', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='price_discount')) if request.POST.get('perm3', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='percentage_discount')) if request.POST.get('perm4', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_SalesReport'), Permission.objects.get(codename='change_SalesReport')) if request.POST.get('permr1', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_StockReport'), Permission.objects.get(codename='change_StockReport')) if request.POST.get('permr2', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_AuditReport'), Permission.objects.get(codename='change_AuditReport')) if request.POST.get('permr5', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='receiptreport')) if request.POST.get('permr3', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='delete_Enquiry')) if request.POST.get('permr6', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='prescriptionreport')) if request.POST.get('permr7', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='adduser')) if request.POST.get('permu1', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='modifyuser')) if request.POST.get('permu2', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='bill')) if request.POST.get('permb1','') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='receipt')) if request.POST.get('permb2', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='delete_AuditReport')) if request.POST.get('permb6', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Appointment'), Permission.objects.get(codename='change_Appointment'), Permission.objects.get(codename='delete_Appointment')) if request.POST.get('permd1','') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Customer'), Permission.objects.get(codename='change_Customer'), Permission.objects.get(codename='delete_Customer')) if request.POST.get('permd6','') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Scan'), Permission.objects.get(codename='change_Scan'), Permission.objects.get(codename='delete_Scan')) if request.POST.get('permd7','') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='change_Enquiry')) if request.POST.get('permd5','') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='viewdoctor')) if request.POST.get('permd4', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='viewpatient')) if request.POST.get('permd2', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='prescribe')) if request.POST.get('permd3', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='change_implementation')) if request.POST.get('permdis1', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='change_inspection')) if request.POST.get('permdis2', '') == 'on' else nop()
        user.save()
        #Create Login History Base
        kwargs = {'user': profile.user, 'profile': profile}
        l = LoginHistory(**kwargs)
        l.save()
        #Send mail[
        kwargs = {'fail_silently': False, 'html_message': My_HTML_Mail(name, username, role, password,organisation), 'recipient_list': [emailid],
         'from_email': 'care@clubayurveda.com', 'message': '', 'subject': 'Welcome to Club Ayurveda'}
        send_mail(**kwargs)
        context['success']=1
        context['message']="User created successfully"
    context['flist'] = Franchise.objects.all().order_by("franchise_name")
    context['perm_template'] = permission_templates(Profile.objects.get(user=request.user).franchise_code)
    template = loader.get_template('app/mydir/adduser.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.adduser', login_url='/page_403.html')
def edituser(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['notify']=0
    if request.method == 'POST':
        id = request.POST.get('id', '')
        name = request.POST.get('name', '')
        username = request.POST.get('username', '')
        emailid = request.POST.get('emailid', '')
        organisation = request.POST.get('organisation','')
        regid = request.POST.get('regid','0')
        if organisation == '':
            organisation = Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0].franchise_name
        role = request.POST.get('role','')
        phoneno = request.POST.get('phoneno','')
        user = User.objects.get(username=username)
        if role=='Vendor':
            organisation = 'Main Office'
            user.user_permissions.add(Permission.objects.get(codename='vendor'))
        if organisation!="Main Office":
            franchise_code = Franchise.objects.filter(franchise_name=organisation).get().id
        else:
            franchise_code = 0 #-- 0 SYMBOLISES MAIN OFFICE
        kwargs = {'user':user, 'name':name, 'role':role, 'organisation':organisation, 'franchise_code':franchise_code, 'regid':regid, 'phoneno':phoneno }
        profile = Profile(id=id, **kwargs)
        profile.save()
        user.user_permissions.clear()
        if request.POST.get('fr_a', '') == 'on':
            user.user_permissions.add(Permission.objects.get(codename='add_franchise'))
        user.user_permissions.add(Permission.objects.get(codename='change_franchise')) if request.POST.get('fr_d', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='delete_franchise')) if request.POST.get('fr_e', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Category'), Permission.objects.get(codename='change_Category'), Permission.objects.get(codename='delete_Category')) if request.POST.get('im_c', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_SKUList'), Permission.objects.get(codename='change_SKUList'), Permission.objects.get(codename='delete_SKUList')) if request.POST.get('im_sku', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Product'), Permission.objects.get(codename='change_Product'), Permission.objects.get(codename='delete_Product')) if request.POST.get('im_pr', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Package'), Permission.objects.get(codename='change_Package'), Permission.objects.get(codename='delete_Package')) if request.POST.get('im_pa', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Service'), Permission.objects.get(codename='change_Service'), Permission.objects.get(codename='delete_Service')) if request.POST.get('im_pa', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Stock'), Permission.objects.get(codename='change_Stock'), Permission.objects.get(codename='delete_Stock')) if request.POST.get('im_sa', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_StockTransfer'), Permission.objects.get(codename='change_StockTransfer'), Permission.objects.get(codename='delete_StockTransfer')) if request.POST.get('im_st', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='itemwise_discount')) if request.POST.get('perm1', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='categorywise_discount')) if request.POST.get('perm2', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='price_discount')) if request.POST.get('perm3', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='percentage_discount')) if request.POST.get('perm4', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_SalesReport'), Permission.objects.get(codename='change_SalesReport'), Permission.objects.get(codename='delete_SalesReport')) if request.POST.get('permr1', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_StockReport'), Permission.objects.get(codename='change_StockReport'), Permission.objects.get(codename='delete_StockReport')) if request.POST.get('permr2', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_AuditReport'), Permission.objects.get(codename='change_AuditReport'), Permission.objects.get(codename='delete_AuditReport')) if request.POST.get('permr5', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='delete_Enquiry')) if request.POST.get('permr6', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='prescriptionreport')) if request.POST.get('permr7', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='adduser')) if request.POST.get('permu1', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='modifyuser')) if request.POST.get('permu2', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='addbill')) if request.POST.get('permb1','') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='viewbill')) if request.POST.get('permb2', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='delete_AuditReport')) if request.POST.get('permb6','') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Appointment'), Permission.objects.get(codename='change_Appointment'), Permission.objects.get(codename='delete_Appointment')) if request.POST.get('permd1','') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Customer'), Permission.objects.get(codename='change_Customer'), Permission.objects.get(codename='delete_Customer')) if request.POST.get('permd6','') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='add_Scan'), Permission.objects.get(codename='change_Scan'), Permission.objects.get(codename='delete_Scan')) if request.POST.get('permd7','') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='change_Enquiry')) if request.POST.get('permd5','') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='viewdoctor')) if request.POST.get('permd4', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='viewpatient')) if request.POST.get('permd2', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='prescribe')) if request.POST.get('permd3', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='change_implementation')) if request.POST.get('permdis1', '') == 'on' else nop()
        user.user_permissions.add(Permission.objects.get(codename='change_inspection')) if request.POST.get('permdis2', '') == 'on' else nop()
        user.save()
        context['success']=1
        context['message']="User edited successfully"
    my_code = Profile.objects.get(user=request.user).franchise_code
    # If get parameter then show details; Else post and go to list of users
    try:
        context['u'] = Profile.objects.get(id=request.GET['id'])
    except:
        return redirect('viewusers')
    if not (my_code==0 or my_code==context['u'].franchise_code):
        context.pop('u')
    perm_list = {}
    for x in Permission.objects.filter(user=context['u'].user):
        perm_list[x.codename] = True
    context['userpermissions'] = perm_list
    try:
        context['fname'] = Franchise.objects.get(id=my_code).franchise_name
    except:
        context['fname'] = "Main Office"
    context['flist'] = Franchise.objects.all().order_by("franchise_name")
    context['perm_template'] = permission_templates(Profile.objects.get(user=request.user).franchise_code)
    template = loader.get_template('app/mydir/edituser.html')
    return HttpResponse(template.render(context, request))


def checkusername(request):
    data={}
    if User.objects.filter(username=request.GET['username']).exists():
        data['message'] = 'Username already exists'
        data['colour'] = '#990000'
    else:
        data['message'] = 'Valid username'
        data['colour'] = '#009900'
    return JsonResponse(data)


@permission_required('app.adduser', login_url='/page_403.html')
def viewusers(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    fc = Profile.objects.filter(user=request.user)[0].franchise_code
    if fc == 0:  #<-- Main Office
        context['user_list'] = Profile.objects.filter().order_by("franchise_code")
    else:
        context['user_list'] = Profile.objects.filter(franchise_code=fc).exclude(user=request.user)
    template = loader.get_template('app/mydir/viewusers.html')
    return HttpResponse(template.render(context, request))


def suspenduser(request):
    data = {}
    try:
        if request.GET['deluser']:
            u = User.objects.get(username=request.GET['deluser'])
            data = {'delete': 1}
            if Profile.objects.filter(user=u)[0].role=="Doctor":
                if Profile.objects.filter(user=request.user)[0].franchise_code=='0':
                    u.delete()
                else:
                    data = {'delete': 2}
            else:
                u.delete()
    except:
        try:
            if request.GET['sususer']:
                u = User.objects.get(username=request.GET['sususer'])
                u.is_active = not u.is_active
                u.save()
                if u.is_active:
                    kwargs = {'fail_silently': False,
                              'message': "Your ClubAyurveda account has been reactivated.",
                              'recipient_list': [u.email],
                              'from_email': 'care@clubayurveda.com', 'subject': 'ClubAyurveda: Account Reactivation Notification'}
                else:
                    kwargs = {'fail_silently': False,
                              'message': "Your ClubAyurveda account has been suspended. Please contact Admin for clarification",
                              'recipient_list': [u.email],
                              'from_email': 'care@clubayurveda.com',
                              'subject': 'ClubAyurveda: Account Suspension Notification'}
                send_mail(**kwargs)
                data = {'suspend': 1}
        except:
            pass
    return JsonResponse(data)


@permission_required('app.viewdoctor', login_url='/page_403.html')
def doctor_details(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    fc = Profile.objects.filter(user=request.user)[0].franchise_code
    if fc == 0:  # <-- Main Office
        context['doctor_list'] = list(Profile.objects.filter(role='Doctor').order_by("franchise_code"))
    else:
        context['doctor_list'] = list(Profile.objects.filter(role='Doctor', franchise_code=fc))
    for i in range(0,len(context['doctor_list'])):
        context['doctor_list'][i].franchise = Franchise.objects.get(id=context['doctor_list'][i].franchise_code)
    template = loader.get_template('app/mydir/doctor_details.html')
    return HttpResponse(template.render(context, request))


def checkregid(request):
    data={}
    if Profile.objects.filter(regid=request.GET['regid']).exists():
        data['message'] = 'Registration ID already taken'
        data['colour'] = '#990000'
    else:
        data['message'] = 'Valid Registration ID'
        data['colour'] = '#009900'
    return JsonResponse(data)


def loginhistory(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['user_history'] = LoginTimestamps.manager.all()
    template = loader.get_template('app/mydir/loginhistory.html')
    return HttpResponse(template.render(context, request))


def save_login(sender, user, request, **kwargs):
    l = LoginHistory.objects.get(user=user)
    kwargs = {'ref':l}
    obj = LoginTimestamps(**kwargs)
    obj.save()

user_logged_in.connect(save_login)
from django.template import loader
from django.http import HttpResponse
import pdb
import datetime as dt
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required
from helper import *
import app.patients as patients


@permission_required('app.change_customer', login_url='/page_403.html')
def registerpatient(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.method == 'POST':
        name = request.POST.get('name', '')
        emailid = request.POST.get('emailid', '')
        gender = request.POST.get('gender', '')
        gstno = request.POST.get('gstno', '')
        company_name = request.POST.get('company_name', '')
        phoneno = request.POST.get('phoneno', '')
        phoneno_sec = request.POST.get('phoneno2', '')
        address = request.POST.get('address1', '')+request.POST.get('address2', '')
        district = request.POST.get('district', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
        dob = dt.datetime.strptime(request.POST.get('dob', ''),'%Y-%m-%d').date()
        franchise_code = Profile.objects.get(user=request.user).franchise_code
        kwargs = {'name': name, 'emailid': emailid, 'phoneno': phoneno, 'phoneno_sec':phoneno_sec, 'gstno':gstno, 'gender':gender,
                  'company_name':company_name, 'address': address, 'district':district, 'state':state, 'country':country,
                  'dob':dob, 'franchise_code':franchise_code}
        cust = Customer(**kwargs)
        cust.save()
        cust.customer_code = Country.get_patientID(country,state,district)
        cust.save()
        fr = Franchise.objects.get(id=franchise_code)
        fr.new_customers += 1
        fr.save()
        patients.newpatient({'name':name,'pid':cust.customer_code})
        kwargs = {'fail_silently': False,
                  'html_message': My_HTML_Mail_patient(name,cust.customer_code),
                  'recipient_list': [emailid],
                  'from_email': 'care@clubayurveda.com', 'message': '', 'subject': 'Welcome to Club Ayurveda'}
        send_mail(**kwargs)
        context['notify'] = 1
        context['notify_message'] = 'Patient ID - '+cust.customer_code
        context['url'] = '/reception.html?q='+cust.customer_code+'&request='+request.POST.get('request', '-')
    template = loader.get_template('app/mydir/registerpatient.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.change_appointment', login_url='/page_403.html')
def recepetion(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    my_fc = Profile.objects.get(user=request.user).franchise_code
    if my_fc!=0:
        my_f = Franchise.objects.get(id=my_fc)
    if request.method == 'GET':
        try:
            context['patientID'] = request.GET['q']
            f = Customer.objects.filter(customer_code=request.GET['q'])[0]
            if f.franchise_code != my_fc and my_fc != 0:
                context['notmyfranchise'] = True
                context['customercode'] = request.GET['q']
            else:
                context['patientphone'] = f.phoneno
                context['patientname'] = f.name
                try:
                    context['appointment'] = Appointment.objects.filter(franchise=my_f,customer_code=request.GET['q'])[0]
                except IndexError:
                    pass
        except IndexError:
            context['failure'] = 1
            context['message'] = "ID not found"
        except KeyError:
            pass
    if request.method == 'POST':
        ccode = request.POST.get('ccode', '')
        doctor = request.POST.get('doctor', '')
        time = request.POST.get('time', '')
        date = request.POST.get('date', '')
        requested = request.POST.get('request', '')
        customer_name = Customer.objects.filter(customer_code=ccode)[0].name
        formatd = "%m/%d/%Y"
        formatm = "%I : %M %p"
        start_time=dt.datetime.strptime(date+'-'+time,formatd+'-'+formatm)
        kwargs = {'customer_code': request.POST.get('ccode', ''), 'customer_name':customer_name, 'doctor_name': doctor, 'receptionist_name':str(request.user),
                  'franchise': my_f,'start_time':start_time,'request':requested}
        objs = Appointment.objects.filter(customer_code=ccode)
        if len(objs)>0:
            objs.update(**kwargs)
        else:
            appointment = Appointment(**kwargs)
            appointment.save()
    context['doctor'] = Profile.objects.filter(role='Doctor', franchise_code = my_fc)
    if my_fc!=0:
        context['appointments'] = Appointment.objects.filter(franchise = my_f).order_by('start_time')
    else:
        context['appointments'] = Appointment.objects.all().order_by('start_time')
    d = dt.datetime.now()
    context['date'] = d.strftime("%m/%d/%Y")
    context['time'] = roundTime(d,roundTo=10*60)
    context['services'] = Service.objects.all()
    context['packages'] = Package.objects.all()
    template = loader.get_template('app/mydir/reception.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.change_enquiry', login_url='/page_403.html')
def enquiry(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    my_code = Profile.objects.get(user=request.user).franchise_code
    if my_code==0:
        context['enquiries'] = Enquiry.objects.filter(cleared=False)
        context['ho'] = True
    else:
        context['enquiries'] = Enquiry.objects.filter(cleared=False, franchise_code=my_code)
    template = loader.get_template('app/mydir/enquiry.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='login.html')
def changeenquirystatus(request):
    e_id = request.GET.getlist('metalist[]')[0]
    status = request.GET.getlist('metalist[]')[1]
    data = {}
    obj = Enquiry.objects.filter(id=e_id)
    if len(obj) == 0:
        data['success'] = 0
        data['error'] = "Enquiry not found"
    else:
        obj[0].status = status
        obj[0].confirmed_time = None
        if status == "Confirmed":
            date = request.GET.getlist('metalist[]')[2]
            time = request.GET.getlist('metalist[]')[3]
            time = date+"|"+time
            format = "%m/%d/%Y|%I:%M %p"
            start_time = dt.datetime.strptime(time, format)
            obj[0].confirmed_time = start_time
            name = obj[0].name
            time = time.split("|")[0]+' at '+time.split("|")[1]
            kwargs = {'fail_silently': False,
                      'html_message': My_HTML_Mail_enquiry_confirmation(name, time),
                      'recipient_list': [obj[0].email],
                      'from_email': 'care@clubayurveda.com', 'message': '', 'subject': 'Club Ayurveda: Appointment Confirmation'}
            send_mail(**kwargs)
        if status=="Cancelled":
            obj[0].cleared = True
        obj[0].lastchanged = dt.datetime.now()
        obj[0].save()
        data['success'] = 1
    return JsonResponse(data)


@login_required(login_url='login.html')
def clearenquiry(request):
    e_id = request.GET.get('e_id')
    data = {}
    obj = Enquiry.objects.filter(id=int(e_id))
    if len(obj) == 0:
        data['success'] = 0
        data['error'] = "Enquiry not found"
    else:
        obj[0].cleared = True
        obj[0].save()
        data['success'] = 1
    return JsonResponse(data)
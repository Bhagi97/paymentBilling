from django.template import loader
from django.http import HttpResponse
import pdb
import datetime as dt
from PyPDF2 import PdfFileMerger
from django.shortcuts import redirect
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Sum
import time
import app.patients as patients
import app.genpre as genpre
from helper import *



@permission_required('app.prescribe', login_url='/page_403.html')
def prescription(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.method == 'GET':
        my_fc = Profile.objects.get(user=request.user).franchise_code
        try:
            c = Customer.objects.get(customer_code=request.GET['q'])
            if c.franchise_code != my_fc:
                context['notmyfranchise'] = True
                context['customercode'] = request.GET['q']
            else:
               try:
                    context['patientID'] = request.GET['q']
                    if len(PendingPrescription.objects.filter(customer_code=context['patientID'])) + len(PendingTreatment.objects.filter(customer_code=context['patientID'])) != 0:
                        return redirect('/editprescription.html?id='+context['patientID'])
                    f = Customer.objects.get(customer_code=request.GET['q'])
                    context['patientphone'] = f.phoneno
                    context['patientname'] = f.name
               except:
                   pass
        except:
            pass # Simple Get
    if request.method == 'POST':
        num_med = (len(request.POST)-13)/4
        my_profile = Profile.objects.get(user=request.user)
        data={}
        data['procedure'] = request.POST.get('procedure', '')
        data['diagnosis'] = request.POST.get('diagnosis', '')
        data['medications'] = request.POST.get('medications', '')
        data['advice'] = request.POST.get('advice', '')
        data['dietadvice'] = request.POST.get('dietadvice', '')
        data['treatmentsuggested'] = request.POST.get('treatmentsuggested', '')
        data['followupdate'] = request.POST.get('followupdate', '')
        data['height'] = request.POST.get('height', '')
        data['weight'] = request.POST.get('weight', '')
        data['doctor'] = str(request.user)
        data['prescription_id'] = IDGenerator.get_id("Prescription",my_profile.franchise_code)
        cfees = request.POST.get('cfees',0)
        if cfees=='':
            cfees = 0
        kwargs = {'customer_code': request.POST.get('ccode', ''), 'customer_name': request.POST.get('name', ''),
                  'doctor_name': my_profile.name,
                  'franchise_code': my_profile.franchise_code,
                  'consultation_fees': cfees}
        med_data={}
        tr_data={}
        mi,ti=0,0
        for i in range(1,num_med+1):
            if request.POST.get('type'+str(i), '')=='Medicine':
                med_data[str(mi)]=[]
                med_data[str(mi)].append(request.POST.get('type'+str(i), ''))
                med_data[str(mi)].append(Product.objects.get(id=int(request.POST.get('medicine'+str(i), ''))).item_name)
                med_data[str(mi)].append(request.POST.get('quantity'+str(i)) if request.POST.get('quantity'+str(i))!="" else '1')
                med_data[str(mi)].append(request.POST.get('dosage'+str(i), ''))
                med_data[str(mi)].append(request.POST.get('medicine' + str(i), ''))
                mi+=1
            else:
                tr_data[str(ti)] = []
                tr_data[str(ti)].append(request.POST.get('type' + str(i), ''))
                tr_data[str(ti)].append(request.POST.get('medicine' + str(i), ''))
                tr_data[str(ti)].append(request.POST.get('quantity' + str(i), '1') if request.POST.get('quantity'+str(i))!="" else '1')
                tr_data[str(ti)].append(request.POST.get('dosage' + str(i), ''))
                ti+=1
        data['pending_trpr'] = 0
        data['pending_medpr'] = 0
        if ti:
            pend_tr = PendingTreatment(**kwargs)
            pend_tr.save()
            kwargs.pop('consultation_fees',None)
            data['treatment'] = tr_data
            data['pending_trpr'] = 1
        if mi:
            pend_pr = PendingPrescription(**kwargs)
            pend_pr.save()
            data['prescription'] = med_data
            data['pending_medpr'] = 1
        patients.insertprescription(request.POST.get('ccode', ''),data)
        context['notify'] = 1
    template = loader.get_template('app/mydir/prescription_new.html')
    context['medicine'] = Product.objects.all().order_by("item_name")
    return HttpResponse(template.render(context, request))


@permission_required('app.prescribe', login_url='/page_403.html')
def prescriptions_made(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['prescriptionlist1'] = PendingPrescription.objects.filter(doctor_name=str(request.user))
    ex_list = context['prescriptionlist1'].values('customer_code')
    context['prescriptionlist2'] = PendingTreatment.objects.filter(doctor_name=str(request.user)).exclude(customer_code__in=ex_list)

    template = loader.get_template('app/mydir/prescriptionsmade.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.prescribe', login_url='/page_403.html')
def edit_prescription(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.method == 'GET':
        id = request.GET['id']
        if not PendingPrescription.objects.filter(doctor_name=Profile.objects.get(user=request.user).name, customer_code=id):
            if not PendingTreatment.objects.filter(doctor_name=Profile.objects.get(user=request.user).name, customer_code=id):
                return redirect('prescriptions_made')
        context['patientID'] = id
        #Get cfees
        try:
            context['cfees'] = PendingTreatment.objects.get(doctor_name=Profile.objects.get(user=request.user).name, customer_code=id).consultation_fees
        except:
            context['cfees'] = PendingPrescription.objects.get(doctor_name=Profile.objects.get(user=request.user).name, customer_code=id).consultation_fees
        f = Customer.objects.get(customer_code=id)
        context['patientphone'] = f.phoneno
        context['patientname'] = f.name
        file_data = patients.getdetails(id)
        for key in range(0,len(file_data)):
            try:
                if file_data[key]['pending_medpr'] == 1 or file_data[key]['pending_trpr'] == 1:
                    pre_details = file_data[key]
                    # MERGE PRESCRIPTION+=TREATMENT
                    for key in pre_details['prescription'].keys():
                        pre_details['prescription'][str(key)][1] = Product.objects.filter(item_name=pre_details['prescription'][str(key)][1], franchise_code__in=[0, f.franchise_code])[0].id
                    if 'prescription' not in pre_details:
                        pre_details['prescription'] = {}
                    if 'treatment' in pre_details:
                        for key,value in pre_details['treatment'].items():
                            pre_details['prescription'][str(len(pre_details['prescription']))] = value
                    # ---
                    context['details'] = pre_details
                    break
            except KeyError:
                pass
        context['medicine'] = Product.objects.all().order_by("item_name")
        context['packages'] = Package.objects.all().order_by("name")
        context['services'] = Service.objects.all().order_by("name")
        context['treatments'] = Treatment.objects.all().order_by("name")
    elif request.method == 'POST':
        num_med = (len(request.POST) - 14) / 4
        file_data = patients.getdetails(request.POST.get('ccode', ''))
        prescription_id = ''
        for key in range(0,len(file_data)):
            try:
                if file_data[key]['pending_medpr'] == 1 or file_data[key]['pending_trpr'] == 1 :
                    prescription_id =  file_data[key]['prescription_id']
                    patients.deleterecord(file_data[key]['_id'])
                    break
            except KeyError:
                pass
        # ----------
        data = {}
        data['procedure'] = request.POST.get('procedure', '')
        data['diagnosis'] = request.POST.get('diagnosis', '')
        data['medications'] = request.POST.get('medications', '')
        data['dietadvice'] = request.POST.get('dietadvice', '')
        data['treatmentsuggested'] = request.POST.get('treatmentsuggested', '')
        data['advice'] = request.POST.get('advice', '')
        data['followupdate'] = request.POST.get('followupdate', '')
        data['height'] = request.POST.get('height', '')
        data['weight'] = request.POST.get('weight', '')
        data['doctor'] = str(request.user)
        data['prescription_id'] = prescription_id
        cfees = request.POST.get('cfees', 0)
        if cfees == '':
            cfees = 0
        med_data = {}
        tr_data = {}
        mi, ti = 0, 0
        for i in range(1, num_med + 1):
            if request.POST.get('type' + str(i), '') == 'Medicine':
                med_data[str(mi)] = []
                med_data[str(mi)].append(request.POST.get('type' + str(i), ''))
                med_data[str(mi)].append(Product.objects.get(id=int(request.POST.get('medicine' + str(i), ''))).item_name)
                med_data[str(mi)].append(request.POST.get('quantity' + str(i), '1') if request.POST.get('quantity'+str(i))!="" else '1')
                med_data[str(mi)].append(request.POST.get('dosage' + str(i), ''))
                med_data[str(mi)].append(request.POST.get('medicine' + str(i), ''))
                mi += 1
            else:
                tr_data[str(ti)] = []
                tr_data[str(ti)].append(request.POST.get('type' + str(i), ''))
                tr_data[str(ti)].append(request.POST.get('medicine' + str(i), ''))
                tr_data[str(ti)].append(request.POST.get('quantity' + str(i), '1') if request.POST.get('quantity'+str(i))!="" else '1')
                tr_data[str(ti)].append(request.POST.get('dosage' + str(i), ''))
                ti += 1
        my_profile = Profile.objects.get(user=request.user)
        kwargs = {'customer_code': request.POST.get('ccode', ''), 'customer_name': request.POST.get('name', ''),
                  'doctor_name': my_profile.name,
                  'franchise_code': my_profile.franchise_code,
                  'consultation_fees': cfees}
        data['pending_trpr'] = 0
        data['pending_medpr'] = 0
        if ti:
            pt,c = PendingTreatment.objects.get_or_create(customer_code=kwargs['customer_code'],franchise_code=my_profile.franchise_code)
            PendingTreatment.objects.filter(id=pt.id).update(**kwargs)
            kwargs.pop('consultation_fees', None)
            data['treatment'] = tr_data
            data['pending_trpr'] = 1
        else:
            PendingTreatment.objects.filter(customer_code=kwargs['customer_code']).delete()
        if mi:
            pp, c = PendingPrescription.objects.get_or_create(customer_code=kwargs['customer_code'], franchise_code=my_profile.franchise_code)
            PendingPrescription.objects.filter(id=pp.id).update(**kwargs)
            data['prescription'] = med_data
            data['pending_medpr'] = 1
        else:
            PendingPrescription.objects.filter(customer_code=kwargs['customer_code']).delete()
        patients.insertprescription(request.POST.get('ccode', ''), data)
        context['notify'] = 1
        # ----------

        return redirect('pending_patients')
    template = loader.get_template('app/mydir/editprescription.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.viewpatient', login_url='/page_403.html')
def patient_details(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.method == 'GET':
        my_fc = Profile.objects.get(user=request.user).franchise_code
        try:
            c = Customer.objects.get(customer_code=request.GET['q'])
            if c.franchise_code != my_fc and my_fc != 0:
                context['notmyfranchise'] = True
                context['customercode'] = request.GET['q']
            else:
                context['patient'] = Customer.objects.get(customer_code=request.GET['q'])
                today = dt.date.today()
                born = context['patient'].dob
                context['patient'].age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
                #Range may or may not be in GET dictionary
                try:
                    context['history'] = patients.getdetails(request.GET['q'],request.GET['range'])
                except:
                    context['history'] = patients.getdetails(request.GET['q'])
        except:
           pass

    context['medicine'] = Product.objects.all().order_by("item_name")
    template = loader.get_template('app/mydir/patient_details.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.prescribe', login_url='/page_403.html')
def pending_patients(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.GET.get('delID'):
        Appointment.objects.filter(customer_code=request.GET.get('delID')).delete()
    context['appointments'] = Appointment.objects.filter(
        franchise__id=Profile.objects.filter(user=request.user)[0].franchise_code,
        doctor_name=request.user).order_by('start_time')
    template = loader.get_template('app/mydir/pending_patients.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.viewpatient', login_url='/page_403.html')
def viewpatients(request):
    perm_list = {}
    myfc = Profile.objects.get(user=request.user).franchise_code
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if myfc==0:
        context['customers']=list(Customer.objects.all())
    else:
        context['customers'] = list(Customer.objects.filter(franchise_code=myfc))
    for i in range(0, len(context['customers'])):
        if context['customers'][i].franchise_code and context['customers'][i].franchise_code != 0:
            context['customers'][i].franchise = Franchise.objects.get(id=context['customers'][i].franchise_code)
            today = dt.date.today()
            born = context['customers'][i].dob
            context['customers'][i].age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    template = loader.get_template('app/mydir/viewpatients.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.change_scan', login_url='/page_403.html')
def upload_scans(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    my_profile = Profile.objects.get(user=request.user)
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        name = request.POST.get('name', '')
        customer_code = request.POST.get('patient', '')
        patient = Customer.objects.get(customer_code=customer_code)
        try:
            image = request.FILES['scan']
        except:
            image = None
        kwargs = {'name': name, 'patient': patient, 'image':image}
        scan = Scan(**kwargs)
        scan.save()
        context['success'] = 1
    template = loader.get_template('app/mydir/upload.html')
    try:
        if perm_list['ho']:
            context['patients'] = Customer.objects.all().order_by("name")
    except KeyError:
        context['patients'] = Customer.objects.filter(franchise_code = my_profile.franchise_code).order_by("name")
    return HttpResponse(template.render(context, request))


def getscans(request):
    id = request.GET.getlist('metalist[]')[0]
    my_code = Profile.objects.get(user=request.user).franchise_code
    data = list(Scan.objects.filter(patient__customer_code=id).values())
    for i in range(0,len(data)):
        data[i]['timestamp'] = data[i]['timestamp'].strftime("%d/%m/%Y")
        data[i]['image'] = 'media/'+data[i]['image']
    data = str(data)
    data = '{ "items": ' + data + ' }'
    data = ast.literal_eval(data)
    return JsonResponse(data)


def delscan(request):
    id = request.GET.get('id')
    data = {}
    Scan.objects.get(id=id).delete()
    data['response'] = 1
    return JsonResponse(data)


def patientreport(request):
    id = request.GET.get('id')
    range = request.GET.get('range')
    c = Customer.objects.get(customer_code=id)
    try:
        f = Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0]
    except IndexError:
        f = Franchise(franchise_name="Main Office")
    meta = {'customer': c, 'franchise': f}
    file_data = patients.getdetails(id,range)

    #List of filenames to concat at the end
    filenames = []
    #For each prescription, generate reports
    for key in xrange(len(file_data)):
        meta['prescription'] = file_data[key]
        pro = []
        arr = meta['prescription'].get('prescription',{})
        for i in arr.keys():
            try:
                pro.append({'product': Product.objects.filter(item_name=arr[i][1])[0], 'quantity': arr[i][2], 'dosage': arr[i][3]})
            except:
                try:
                    pro.append({'product': Package.objects.filter(name=arr[i][1])[0], 'quantity': arr[i][2], 'dosage': arr[i][3]})
                except:
                    try:
                        pro.append({'product': Service.objects.filter(name=arr[i][1])[0], 'quantity': arr[i][2], 'dosage': arr[i][3]})
                    except:
                        try:
                            pro.append({'product': Treatment.objects.filter(name=arr[i][1], franchise_code=
                            Profile.objects.filter(user=request.user)[0].franchise_code).get(), 'quantity': arr[i][2],
                                        'dosage': arr[i][3]})
                        except:
                            print("Prescription Print Error")
        arr = meta['prescription'].get('treatment', {})
        for i in arr.keys():
            try:
                pro.append({'product': Product.objects.filter(item_name=arr[i][1])[0], 'quantity': arr[i][2], 'dosage': arr[i][3]})
            except:
                try:
                    pro.append({'product': Package.objects.filter(name=arr[i][1])[0], 'quantity': arr[i][2], 'dosage': arr[i][3]})
                except:
                    try:
                        pro.append({'product': Service.objects.filter(name=arr[i][1])[0], 'quantity': arr[i][2], 'dosage': arr[i][3]})
                    except:
                        try:
                            pro.append({'product': Treatment.objects.filter(name=arr[i][1], franchise_code=
                            Profile.objects.filter(user=request.user)[0].franchise_code).get(), 'quantity': arr[i][2],
                                        'dosage': arr[i][3]})
                        except:
                            print("Prescription Print Error")
        filename = User.objects.make_random_password(length=15)
        meta['filename'] = filename
        meta['date'] = file_data[key]['datetime'].strftime("%dth %B, %Y")
        genpre.generatepdf(pro, meta)
        filenames.append(filename)
    #Cover page
    filename = User.objects.make_random_password(length=15)
    meta['filename'] = filename
    meta['range'] = range
    genpre.generatecover(meta)
    filenames.append(filename)
    #Combine pdfs
    merger = PdfFileMerger()
    prefix = '/var/www/html/media/bill/'
    for pdf in reversed(filenames):
        merger.append(prefix+pdf+".pdf")
    filename = User.objects.make_random_password(length=15)
    merger.write(prefix+filename+".pdf")
    return JsonResponse({'url': '/media/bill/'+filename+".pdf"})


@permission_required('app.viewpatient', login_url='/page_403.html')
def medicalreports(request):
    return redirect('patient_details')
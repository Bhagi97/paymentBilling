from django.template import loader
from django.http import HttpResponse
import pdb
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from app.blocks.helper import *


@permission_required('app.add_franchise', login_url='/page_403.html')
def addfranchise(request):
    perm_list={}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename]=True
    context = {'permissions':perm_list}
    context['vendor_list'] = Profile.objects.filter(role='Vendor')
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/mydir/'+load_template)
    return HttpResponse(template.render(context, request))


def checkfranchisename(request):
    data={}
    if Franchise.objects.filter(franchise_name=request.GET['name']).exists():
        data['message'] = 'Franchise already exists'
        data['colour'] = '#990000'
    else:
        data['message'] = 'Valid Franchise name'
        data['colour'] = '#009900'
    return JsonResponse(data)


@permission_required('app.change_franchise', login_url='/page_403.html')
def editfranchise(request):
    perm_list={}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename]=True
    context = {'permissions':perm_list}
    if request.method == 'GET':
        try:
            id=request.GET['id']
            kwargs = {'id': id}
            f = [Franchise.objects.get(**kwargs)]
            context['franchise']=f
            context['id']=id
            countries = []
            qs1 = Country.objects.values_list('country').distinct()
            for c in range(0,len(qs1)):
                countries.append(qs1[c][0])
            states=[]
            qs2= Country.objects.filter(country=f[0].country).values_list('state').distinct()
            for c in range(0, len(qs2)):
                states.append(qs2[c][0])
            districts=[]
            qs3 = Country.objects.filter(country=f[0].country,state=f[0].state).values_list('district').distinct()
            for c in range(0,len(qs3)):
                districts.append(qs3[c][0])
            context['countries']=countries
            context['states']=states
            context['districts']=districts
            context['vendor_list'] = Profile.objects.filter(role='Vendor')
        except:
            pass
        load_template = request.path.split('/')[-1]
        template = loader.get_template('app/mydir/' + load_template)

        return HttpResponse(template.render(context, request,))


@login_required(login_url='login.html')
def viewfranchise(request):
    perm_list={}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename]=True
    context = {'permissions':perm_list}
    if request.method == 'POST':
        try:
            if request.GET['id']:
                f = Franchise.objects.get(id=int(request.GET['id']))
                keys = [key.name for key in Franchise._meta.get_fields()]
                keys.remove("id")
                for k in keys:
                    if k.find('perm')==0:
                        setattr(f,k,map_str_to_bool(request.POST.get(k)))
                    elif request.POST.get(k,'') != "":
                        setattr(f, k, request.POST.get(k))
                f.save()
        except:
            franchise_name = request.POST.get('franchise-name','')
            franchise_type = request.POST.get('franchise-type','')
            franchise_code = int(request.POST.get('franchise-code',0))
            phoneno = request.POST.get('phoneno', '')
            address = request.POST.get('address', '')
            town = request.POST.get('town', '')
            district = request.POST.get('district', '')
            state = request.POST.get('state', '')
            country = request.POST.get('country', '')
            pincode = request.POST.get('pincode', '')
            bankaccountno = request.POST.get('bankaccountno', '')
            bankname = request.POST.get('bankname', '')
            ifsccode = request.POST.get('ifsccode', '')
            gstno = request.POST.get('gstno', '')
            druglicenseno = request.POST.get('dlo', '').upper()
            website = request.POST.get('website', '')
            owner = request.POST.get('owner', '')
            ownercontact = request.POST.get('ownercontact', '')
            vendor = Profile.objects.get(id=int(request.POST.get('vendor', '')))
            remarks = request.POST.get('remarks', '')
            currency = True if request.POST.get('currency', '') == 'on' else False
            permbs1 = True if request.POST.get('permbs1', '') == 'on' else False
            permbs2 = True if request.POST.get('permbs2', '') == 'on' else False
            permb3 = True if request.POST.get('permb3', '') == 'on' else False
            permb4 = True if request.POST.get('permb4', '') == 'on' else False
            permb5 = True if request.POST.get('permb5', '') == 'on' else False
            kwargs = {'franchise_name':franchise_name,'franchise_type':franchise_type,
                        'phoneno':phoneno,'address':address,'town':town,'district':district,'state':state,'country':country,'pincode':pincode,
                        'website': website, 'gstno': gstno, 'druglicenseno': druglicenseno, 'bankaccountno': bankaccountno, 'bankname': bankname, 'ifsccode': ifsccode,
                        'owner':owner,'ownercontact':ownercontact, 'vendor':vendor, 'remarks':remarks, 'permbs1':permbs1, 'permbs2':permbs2,
                        'currency':currency,'permb3':permb3,'permb4':permb4,'permb5':permb5}
            if franchise_code:
                franchise_obj = Franchise(id=franchise_code,**kwargs)
            else:
                franchise_obj = Franchise(**kwargs)
            franchise_obj.save()
            id = franchise_obj.id
            #Create ID Generator rows
            IDGenerator(name="Prescription",franchise_code=id).save()
            IDGenerator(name="Bill",franchise_code=id).save()
            IDGenerator(name="Receipt",franchise_code=id).save()
            #CREATE ADMIN
            if franchise_code==0:
                name = owner
                username = request.POST.get('username', '')
                emailid = request.POST.get('emailid', '')
                password = User.objects.make_random_password(length=6)
                organisation = franchise_name
                role = "Admin"
                phoneno = ownercontact
                user = User.objects.create_user(username, emailid, password)
                user.save()
                if organisation != "Main Office":
                    franchise_code = id
                else:
                    franchise_code = 0  # -- 0 SYMBOLISES MAIN OFFICE
                kwargs = {'user': user, 'role': role, 'organisation': organisation, 'franchise_code': franchise_code,
                          'name':owner, 'phoneno': phoneno}
                profile = Profile(**kwargs)
                profile.save()
                franchise_obj.admin = profile
                franchise_obj.save()
                user.user_permissions.add(Permission.objects.get(codename='add_Category'),
                                          Permission.objects.get(codename='change_Category'),
                                          Permission.objects.get(codename='delete_Category')) if request.POST.get(
                    'im_c', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='add_SKUList'),
                                          Permission.objects.get(codename='change_SKUList'),
                                          Permission.objects.get(codename='delete_SKUList')) if request.POST.get(
                    'im_sku', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='add_Product'),
                                          Permission.objects.get(codename='change_Product'),
                                          Permission.objects.get(codename='delete_Product')) if request.POST.get(
                    'im_pr', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='add_PackageMask'),
                                          Permission.objects.get(codename='change_PackageMask'),
                                          Permission.objects.get(codename='delete_PackageMask')) if request.POST.get(
                    'im_pa', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='add_ServiceMask'),
                                          Permission.objects.get(codename='change_ServiceMask'),
                                          Permission.objects.get(codename='delete_ServiceMask')) if request.POST.get(
                    'im_pa', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='add_Stock'),
                                          Permission.objects.get(codename='change_Stock'),
                                          Permission.objects.get(codename='delete_Stock')) if request.POST.get('im_sa',
                                                                                                               '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='add_StockTransfer'),
                                          Permission.objects.get(codename='change_StockTransfer'),
                                          Permission.objects.get(codename='delete_StockTransfer')) if request.POST.get('im_st',
                                                                                                               '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='itemwise_discount')) if request.POST.get(
                    'perm1', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='categorywise_discount')) if request.POST.get(
                    'perm2', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='price_discount')) if request.POST.get(
                    'perm3', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='percentage_discount')) if request.POST.get(
                    'perm4', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='add_SalesReport'),
                                          Permission.objects.get(codename='change_SalesReport'),
                                          ) if request.POST.get(
                    'permr1', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='add_StockReport'),
                                          Permission.objects.get(codename='change_StockReport'),
                                          ) if request.POST.get(
                    'permr2', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='add_AuditReport'),
                                          Permission.objects.get(codename='change_AuditReport'),
                                          ) if request.POST.get(
                    'permr5', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='receiptreport')) if request.POST.get(
                    'permr3', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='delete_Enquiry')) if request.POST.get(
                    'permr6', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='prescriptionreport')) if request.POST.get(
                    'permr7', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='adduser')) if request.POST.get('permu1',
                                                                                                          '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='modifyuser')) if request.POST.get('permu2',
                                                                                                             '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='bill')) if request.POST.get('permb1',
                                                                                                       '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='receipt')) if request.POST.get('permb2',
                                                                                                          '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='add_Appointment'),
                                          Permission.objects.get(codename='change_Appointment'),
                                          Permission.objects.get(codename='delete_Appointment')) if request.POST.get(
                    'permd1', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='add_Customer'),
                                          Permission.objects.get(codename='change_Customer'),
                                          Permission.objects.get(codename='delete_Customer')) if request.POST.get(
                    'permd6', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='add_Scan'),
                                          Permission.objects.get(codename='change_Scan'),
                                          Permission.objects.get(codename='delete_Scan')) if request.POST.get('permd7',
                                                                                                              '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='change_Enquiry')) if request.POST.get(
                    'permd5', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='viewdoctor')) if request.POST.get('permd4',
                                                                                                             '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='viewpatient')) if request.POST.get('permd2',
                                                                                                              '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='prescribe')) if request.POST.get('permd3',
                                                                                                            '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='change_implementation')) if request.POST.get(
                    'permdis1', '') == 'on' else nop()
                user.user_permissions.add(Permission.objects.get(codename='change_inspection')) if request.POST.get(
                    'permdis2', '') == 'on' else nop()
                user.save()

                # Create Login History Base
                kwargs = {'user': profile.user, 'profile': profile}
                l = LoginHistory(**kwargs)
                l.save()
                # Send mail
                kwargs = {'fail_silently': False,
                          'html_message': My_HTML_Mail(name, username, role, password, organisation),
                          'recipient_list': [emailid],
                          'from_email': 'care@clubayurveda.com', 'message': '', 'subject': 'Welcome to Club Ayurveda'}
                send_mail(**kwargs)
                context['success'] = 1
                context['message'] = "Franchisee created successfully"

    f_list = Franchise.objects.all().order_by("franchise_name")
    if request.method == 'GET':
        try:
            criteria=request.GET['q']
            kwargs={'franchise_name__contains':criteria}
            f_list = Franchise.objects.filter(**kwargs).order_by("franchise_name")
        except:
            f_list = Franchise.objects.all().order_by("id")[:10]

    context['franchise_list'] = f_list
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/mydir/'+load_template)
    return HttpResponse(template.render(context, request))


def suspendfranchise(request):
    data = {}
    try:
        if request.GET['delcode']:
            ps = Profile.objects.filter(franchise_code=request.GET['delcode'])
            for p in ps:
                p.user.delete()
            Franchise.objects.get(id=request.GET['delcode']).delete()
            #DELETE FROM NECESSARY INFO FROM ALL TABLES
            data = {'delete': 1}
    except:
        try:
            if request.GET['suscode']:
                ps = Profile.objects.filter(franchise_code=request.GET['suscode'])
                for p in ps:
                    p.user.is_active = not p.user.is_active
                    p.user.save()
                f = Franchise.objects.get(id=request.GET['suscode'])
                f.active = not f.active
                f.save()
                if f.active:
                    kwargs = {'fail_silently': False,
                              'message': "Your ClubAyurveda franchise has been reactivated.",
                              'recipient_list': [f.admin.user.email],
                              'from_email': 'care@clubayurveda.com', 'subject': 'ClubAyurveda: Account Reactivation Notification'}
                else:
                    kwargs = {'fail_silently': False,
                              'message': "Your ClubAyurveda franchise has been suspended. Please contact Main Office for clarification",
                              'recipient_list': [f.admin.user.email],
                              'from_email': 'care@clubayurveda.com',
                              'subject': 'ClubAyurveda: Account Suspension Notification'}
                send_mail(**kwargs)
                data = {'suspend': 1}
        except:
            pass
    return JsonResponse(data)


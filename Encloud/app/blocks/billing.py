from django.template import loader
from django.http import HttpResponse
import pdb
import json
import datetime as dt
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import permission_required,login_required
from django.shortcuts import redirect
import app.patients as patients
from helper import *
import app.genpre as genpre
import app.genbill as genbill
import app.reportmanager as reportmanager


@permission_required('app.bill', login_url='/page_403.html')
def newbill(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['franchise_code'] = Profile.objects.get(user=request.user).franchise_code
    # HO Inventory
    if request.method == 'POST':
        id = request.POST.get('id', '')
        name = request.POST.get('name', '')
        rate = float(request.POST.get('rate', ''))
        tax_cgst = float(request.POST.get('tax_cgst', ''))
        tax_sgst = float(request.POST.get('tax_sgst', ''))
        stock = int(request.POST.get('stock', 0))
        kwargs = {'item_name': name, 'MRP': rate, 'tax_CGST': tax_cgst,'tax_SGST':tax_sgst,
                  'stock': stock}
        if id!='':
            obj = HOProduct(id=id, **kwargs)
        else:
            obj = HOProduct(**kwargs)
        obj.save()
    if context['franchise_code']==0:
        context['itemlist'] = HOProduct.objects.all().order_by("item_name")
        context['sku'] = SKUList.objects.all()
        context['flist'] = Franchise.objects.all()
    else:
        context['categorylist'] = Category.objects.all().order_by("category_name")
    template = loader.get_template('app/mydir/newbill.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.bill', login_url='/page_403.html')
def invoicebill(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if Profile.objects.get(user=request.user).franchise_code == 0:
        return redirect('newbill')
    template = loader.get_template('app/mydir/invoicebill.html')
    return HttpResponse(template.render(context, request))


def savebill(request):
    pl = request.GET.getlist('productlist[]')
    ml = request.GET.getlist('metalist[]')
    rl = request.GET.getlist('ratelist[]')
    dl = request.GET.getlist('durationlist[]')
    c = Customer.objects.filter(customer_code=ml[0])
    if len(c) == 0:
        return JsonResponse({'success':0})
    else:
        c = c[0]
        kwargs = {'customer_code': c.customer_code,
                  'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code,
                  'doctor': str(ml[1]),
                  'productlist': str(pl),
                  'durationlist': str(dl),
                  'ratelist': str(rl)}
        objs = SavedBill.objects.filter(customer_code=c.customer_code)
        if len(objs) > 0:
            objs.update(**kwargs)
        else:
            bill = SavedBill(**kwargs)
            bill.save()
    return JsonResponse({'success':1})


def printinvoice(request):
    pl = request.GET.getlist('productlist[]')
    ml = request.GET.getlist('metalist[]')
    rl = request.GET.getlist('ratelist[]')
    recl = request.GET.getlist('receiptlist[]')
    robj = json.loads(request.GET.get('robj'))
    dl = request.GET.getlist('durationlist[]')
    c = Customer.objects.filter(customer_code=ml[0])
    if len(c)==0:
        c = ''
    else:
        c=c[0]
    f = Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0]
    meta={'customer':c, 'franchise':f}
    pro = []
    for i in range(0, len(pl)):
        try:
            discount = Discount.objects.filter(sid__name=pl[i])
            pro.append({'product': Service.objects.filter(name=pl[i]).get(), 'rate':-1, 'quantity':1, 'discount':discount})
        except:
            try:
                discount = Discount.objects.filter(pid__name=pl[i])
                pro.append({'product': Package.objects.filter(name=pl[i]).get(), 'rate':-1, 'quantity':1, 'discount':discount})
            except:
                try:
                    discount = Discount.objects.filter(tid__name=pl[i], franchise_code=meta['franchise'].id)
                    product = Treatment.objects.filter(name=pl[i], franchise_code=meta['franchise'].id).get()
                    duration = TreatmentMaster.objects.get(name=product.name).duration
                    if dl[i]:
                        rate = round(float(dl[i])/duration)*product.rate
                    else:
                        rate = float(product.rate)
                    pro.append({'product':product , 'rate':rate,'quantity':1, 'discount':discount})
                except:
                    pro.append({'product':wrapper(pl[i],int(rl[i])), 'rate':rl[i], 'quantity': 1, 'stock':'','discount':[]})
    #Generate receipt
    meta['receipt_filename'],rid = generatereceipt(robj,c,request.user)
    recl.append(rid)
    #Geneate bill
    filename = User.objects.make_random_password(length=15)
    meta['filename'] = filename
    meta['company_flag'] = int(ml[2])
    meta['doctor'] = ml[3]
    meta['discount_type'] = ml[4]
    meta['discount_value'] = float(ml[5])
    if meta['company_flag']:
        c.company_name = ml[1]
        c.save()
    meta['bill_id'] = IDGenerator.get_id("Bill", meta['franchise'].id)
    reportmanager.manage(meta, pro)
    total = genbill.ibillpdf(meta, pro)
    linkreceipts(meta['bill_id'],recl)
    #Update display data
    f.sales_today += total
    f.customers_today += 1
    f.save()
    SavedBill.objects.filter(customer_code=ml[0]).delete()
    return JsonResponse({'filename':filename,'receipt_filename':meta['receipt_filename']})


def getsavedbill(request):
    id = request.GET.getlist('ID[]')[0].upper()
    res = Customer.objects.filter(customer_code=id)
    if len(res) == 1:
        if Profile.objects.get(user=request.user).franchise_code != res[0].franchise_code:
            return JsonResponse({'success':2,'doctor':''})
        objs = SavedBill.objects.filter(customer_code=id)
        if len(objs)>0:
            ratelist = ast.literal_eval(objs[0].ratelist)
            productlist = ast.literal_eval(objs[0].productlist)
            durationlist = ast.literal_eval(objs[0].durationlist)
            return JsonResponse({'success': 1, 'company_name':res[0].company_name, 'doctor':objs[0].doctor, 'productlist':productlist,'ratelist':ratelist,'durationlist':durationlist})
        else:
            return JsonResponse({'success': 1, 'company_name':res[0].company_name, 'doctor':''})
    else:
        return JsonResponse({'success': 0})



def get_products(request):
    fr_data = {"Brahmi":0,"Tulsi":1,"Arayaal":2,"Ashoka":3}
    type = 'service'
    ind = fr_data[Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0].franchise_type]
    if request.GET['category'] == "Services":
        data = list(Service.objects.all().values())
        for i in range (0,len(data)):
            data[i]=dict(data[i])
            if data[i]['rates'] != '':
                r = ast.literal_eval(data[i]['rates'])
                r1 = r[ind]
                discount = Discount.objects.filter(sid__name=data[i]['name'])
                r2=''
                if len(discount)>0:
                    r2 = int(r1)
                    r1 = round(r1*(1+(data[i]['tax_CGST']+data[i]['tax_CGST'])/100))
                    if discount[0].discount_type == '%':
                        r2 = r1 - int((discount[0].value / 100) * (r2))
                    else:
                        r2 = r1 - int(discount[0].value)
                    r2 = ',' + str(r2)

                data[i]['rates'] = str(r1)
                data[i]['rates'] += r2

    elif request.GET['category'] == "Packages":
        data = list(Package.objects.all().values())
        for i in range (0,len(data)):
            data[i]=dict(data[i])
            if data[i]['rates'] != '':
                r = ast.literal_eval(data[i]['rates'])
                data[i]['rates'] = r[ind]
    elif request.GET['category'] == "Treatments":
        data = list(Treatment.objects.filter(franchise_code=Profile.objects.get(user=request.user).franchise_code).values())
        for i in range (0,len(data)):
            data[i]=dict(data[i])
            data[i]['rates'] = data[i]['rate']
    elif request.GET['category'] == "Miscellaneous":
        data = [{"item_name":"Consultation Fee", "MRP":-1},
                {"item_name":"Extra Charges", "MRP":-1},
                {"item_name":"Yoga", "MRP":-1},
                {"item_name":"Meditation", "MRP":-1},
                # {"item_name":"Registration Fee", "MRP":-1},
                {"item_name":"Bed Charges", "MRP":-1},
                {"item_name":"Clinical Support Services", "MRP":-1},
                {"item_name":"Consumables", "MRP":-1},
                {"item_name":"Food and Beverages", "MRP":-1},
                {"item_name":"Room Rent", "MRP":-1},
                {"item_name":"Discount", "Percentage":-1},]
        type = 'product'
    else:
        data = list(Product.objects.filter(category=request.GET['category']).values())
        type = 'product'
    data = {'products':data}
    data["type"] = type
    return JsonResponse(data)


#To wrap abnormal items such as consultation fees/extra charges
class wrapper:
    def __init__(self,p,r):
        self.MRP=r
        self.tax_CGST=0
        self.tax_SGST=0
        self.item_name=p
        self.discount=0


def printbill(request):
    pl = map(lambda x:int(x), request.GET.getlist('productlist[]'))
    rl = request.GET.getlist('ratelist[]')
    ql = request.GET.getlist('quantitylist[]')
    ml = request.GET.getlist('metalist[]')
    c = Customer.objects.filter(customer_code=ml[0])
    if len(c)==0:
        c = ''
    else:
        c=c[0]
    f = Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0]
    meta={'customer':c, 'franchise':f}
    pro = []
    for i in range(0, len(pl)):
        try:
            stock = Stock.objects.filter(id=pl[i]).get()
            product = Product.objects.filter(id=stock.pid).get()
            discount = Discount.objects.filter(proid__id=stock.pid, franchise_code=meta['franchise'].id)
            pro.append({'product':product, 'quantity':ql[i], 'stock':stock, 'discount':discount})
        except:
            pro.append({'product':wrapper(pl[i],int(rl[i])), 'quantity': 1, 'stock':'N.A.', 'discount':[]})
    success, status = genbill.managestock(pro)
    if success:
        filename = User.objects.make_random_password(length=15)
        meta['filename'] = filename
        meta['doctor'] = ml[3]
        meta['company_flag'] = int(ml[2])
        meta['company_name'] = ml[1]
        if meta['company_flag']:
            if c!='':
                c.company_name = ml[1]
                c.save()
        meta['bill_id'] = IDGenerator.get_id("Bill", meta['franchise'].id)
        reportmanager.manage(meta, pro)
        total = genbill.generatepdf(meta, pro)
        f.sales_today += total
        f.customers_today += 1
        f.save()
        return JsonResponse({'success': success, 'status': status, 'filename': filename})
    else:
        return JsonResponse({'success':success, 'status':status})


def print_hobill(request):
    pl = request.GET.getlist('productlist[]')
    ql = request.GET.getlist('quantitylist[]')
    ml = request.GET.getlist('metalist[]')
    rl = request.GET.getlist('ratelist[]')
    pro = []
    meta = {}
    if ml[0]:
        meta['franchise'] = Franchise.objects.get(id=ml[0])
    for i in range(0, len(pl)):
        pro.append({'product':HOProduct.objects.filter(item_name=pl[i]).get(), 'quantity':ql[i]})
    filename = User.objects.make_random_password(length=15)
    meta['filename'] = filename
    meta['company_flag'] = 0
    meta['bill_id'] = IDGenerator.get_id("Bill", meta['franchise'].id)
    reportmanager.homanage(meta, pro)
    genbill.hogeneratepdf(meta, pro)
    success, status = genbill.homanagestock(meta, pro)
    return JsonResponse({'success':success, 'status':status, 'filename':filename})


def search_id(request):
    id = request.GET.getlist('ID[]')[0].upper()
    # if id.upper()=="SELF":
    #     return JsonResponse({'success':2})
    res = Customer.objects.filter(customer_code=id)
    if len(res)==1:
        if Profile.objects.get(user=request.user).franchise_code == res[0].franchise_code:
            return JsonResponse({'success':1,'company_name':res[0].company_name,'name':res[0].name})
        else:
            return JsonResponse({'success': 2})
    else:
        return JsonResponse({'success': 0})


@permission_required('app.bill', login_url='/page_403.html')
def pending_prescription(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['medprescriptionlist'] = PendingPrescription.objects.filter(franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code).order_by("customer_name")
    context['trprescriptionlist'] = PendingTreatment.objects.filter(franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code).order_by("customer_name")
    template = loader.get_template('app/mydir/pendingprescription.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.bill', login_url='/page_403.html')
def get_pending_prescription(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    id = request.GET['q']
    context['patientID']=id
    context['suffix'] =request.GET['suffix']
    try:
        if context['suffix']=='medpr':
            context['cfees'] = PendingPrescription.objects.filter(customer_code=id)[0].consultation_fees
            context['link'] = '/newbill.html?'
        else:
            context['cfees'] = PendingTreatment.objects.filter(customer_code=id)[0].consultation_fees
            context['link'] = '/invoicebill.html?'
    except IndexError:
        return redirect('pending_prescription')
    pre_details = patients.getprescriptiondata(id,context['suffix'])

    pre_details['rates'] = []
    if request.GET['suffix']=='medpr':
        for key in pre_details['prescription'].keys():
                pre_details['rates'].append(pre_details['prescription'][key][4])
        pre_details.pop('treatment',None)
    else:
        for key in pre_details['treatment'].keys():
            if pre_details['treatment'][key][0]=='Package':
                pre_details['rates'].append(findrate(Package.objects.filter(name=pre_details['treatment'][key][1])[0].rates,Profile.objects.filter(user=request.user)[0].franchise_code))
            elif pre_details['treatment'][key][0]=='Service':
                pre_details['rates'].append(findrate(Service.objects.filter(name=pre_details['treatment'][key][1])[0].rates,Profile.objects.filter(user=request.user)[0].franchise_code))
            elif pre_details['treatment'][key][0]=='Treatment':
                pre_details['rates'].append(Treatment.objects.filter(name=pre_details['treatment'][key][1],franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code)[0].rate)
        pre_details.pop('prescription',None)
        pre_details['prescription'] = pre_details.pop('treatment',None)
    context['details'] = pre_details

    template = loader.get_template('app/mydir/prescription_pending.html')
    return HttpResponse(template.render(context, request))



def printprescription(request):
    m = request.GET.getlist('meta[]')
    dl = request.GET.getlist('dosagelist[]')
    id = m[1]
    suffix = m[2]
    c = Customer.objects.filter(customer_code=id)
    if len(c)==0:
        c = ''
    else:
        c=c[0]
    f = Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0]
    meta={'customer':c, 'franchise':f}
    pre_details = patients.getprescriptiondata(id,m[2])
    if pre_details == None:
        return JsonResponse({'success': 0, 'message': "Prescription already printed"})
    unset_key = 'pending_'+suffix
    meta['doctor']=pre_details['doctor']
    meta['prescription_id']=pre_details['prescription_id']
    meta['followupdate']=pre_details['followupdate']
    meta['prescription'] = pre_details['prescription'] if suffix=='medpr' else pre_details['treatment']
    patients.updatekey(pre_details['_id'],unset_key)

    filename = User.objects.make_random_password(length=15)
    meta['filename'] = filename
    genpre.generateprescription(meta,dl)
    if suffix=="medpr":
        PendingPrescription.objects.filter(customer_code=id).delete()
    else:
        PendingTreatment.objects.filter(customer_code=id).delete()

    return JsonResponse({'success': 1, 'filename':filename})


@permission_required('app.receipt', login_url='/page_403.html')
def receipt(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['franchise_code'] = Profile.objects.get(user=request.user).franchise_code
    if request.method == 'POST':
        type = request.POST.get('type', '')
        method = request.POST.get('method', '')
        if method=="Cash":
            details = request.POST.get('details', '')
        elif method=="Cheque":
            bankname = request.POST.get('bankname', '')
            accountholder = request.POST.get('accountholder', '')
            accountno = request.POST.get('accountno', '')
            chequeno = request.POST.get('chequeno', '')
            dated = request.POST.get('dated', '')
            details = " Bank Name: "+bankname+" | Cheque No: "+chequeno+" | Date: "+\
                      dated+" | Account Holder: "+accountholder+" | Account No: "+accountno
        elif method=="Credit/Debit Card":
            name = request.POST.get('cd_name', '')
            cardno = request.POST.get('cd_cardno', '')
            expiry = request.POST.get('cd_ed', '')
            rno = request.POST.get('cd_rno', '')
            details = " Name: "+name+" | Card No: "+cardno+" | Expiry: "+\
                      expiry+" | Receipt No: "+rno
        else:
            name = request.POST.get('neft_name', '')
            bankname = request.POST.get('neft_bankname', '')
            accountno = request.POST.get('neft_accountno', '')
            details = " Name: "+name+" | Bank Name: "+bankname+" | Account No: "+accountno
        patientid = request.POST.get('patientid', '')
        cashier = Profile.objects.get(user=request.user)
        franchise = Franchise.objects.get(id=cashier.franchise_code)
        customer = Customer.objects.get(customer_code=patientid)
        amount = float(request.POST.get('amount', ''))
        receipt_id = IDGenerator.get_id('Receipt',cashier.franchise_code)
        kwargs = {'amount': amount, 'customer': customer, 'details': details, 'method': method,
                  'type': type, 'cashier':cashier, 'franchise':franchise, 'receipt_id':receipt_id }
        obj = Receipt(**kwargs)
        obj.save()
        context['filename'] = User.objects.make_random_password(length=15)
        genbill.generatereceipt(obj, context['filename'])

    template = loader.get_template('app/mydir/receipt.html')
    return HttpResponse(template.render(context, request))


#To generate balance receipt
def generatereceipt(robj,patient,cashier):
    type = robj.get('type', '')
    method = robj.get('method', '')
    if method == "Cash":
        details = robj.get('details', '')
    elif method == "Cheque":
        bankname = robj.get('bankname', '')
        accountholder = robj.get('accountholder', '')
        accountno = robj.get('accountno', '')
        chequeno = robj.get('chequeno', '')
        dated = robj.get('dated', '')
        details = "Bank Name: " + bankname + " | Cheque No: " + chequeno + " | Date: " + \
                  dated + " | Account Holder: " + accountholder + " | Account No: " + accountno
    elif method == "Credit/Debit Card":
        name = robj.get('cd_name', '')
        cardno = robj.get('cd_cardno', '')
        expiry = robj.get('cd_ed', '')
        rno = robj.get('cd_rno', '')
        details = " Name: " + name + " | Card No: " + cardno + " | Expiry: " + \
                  expiry + " | Receipt No: " + rno
    else:
        name = robj.get('neft_name', '')
        bankname = robj.get('neft_bankname', '')
        accountno = robj.get('neft_accountno', '')
        details = "Name: " + name + " | Bank Name: " + bankname + " | Account No: " + accountno
    customer = patient
    cashier = Profile.objects.get(user=cashier)
    franchise = Franchise.objects.get(id=cashier.franchise_code)
    amount = float(robj.get('amount', ''))
    receipt_id = IDGenerator.get_id('Receipt', cashier.franchise_code)
    kwargs = {'amount': amount, 'customer': customer, 'details': details, 'method': method,
              'type': type, 'cashier': cashier, 'franchise': franchise, 'receipt_id':receipt_id}
    obj = Receipt(**kwargs)
    obj.save()
    filename = User.objects.make_random_password(length=15)
    genbill.generatereceipt(obj, filename)
    return filename,obj.id


def getreceipts(request):
    id = request.GET.get('id').upper()
    if id=="SELF":
        return JsonResponse({'success':2})
    res = Customer.objects.filter(customer_code=id)
    if len(res)==1:
        receipts = list(Receipt.objects.filter(customer__customer_code=id,bill=None).values())
        for i in range(0,len(receipts)):
            receipts[i]['date'] = receipts[i]['date'].strftime("%d/%m/%Y %I:%M %p")
        return JsonResponse({'success':1,'receipts':receipts})
    else:
        return JsonResponse({'success': 0})


def linkreceipts(bill_id, recl):
    bill = SalesReportBase.objects.get(bill_id=bill_id)
    for id in recl:
        obj = Receipt.objects.get(id=int(id))
        obj.bill = bill
        obj.save()
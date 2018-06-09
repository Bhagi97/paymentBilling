from django.template import loader
from django.http import HttpResponse
from app.forms import *
import pdb
import datetime as dt
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import permission_required
from app.blocks.helper import *
from django.shortcuts import redirect

@permission_required('app.add_category', login_url='/page_403.html')
def categoryentry(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['success']=0               # - Indicate successful insertion of category into database
    if request.method == 'POST':
        category_id= request.POST.get('category_id', '')
        category_name = request.POST.get('category_name', '')
        category_code = request.POST.get('category_code', '')
        category_description = request.POST.get('category_description', '')
        kwargs = {'category_name': category_name, 'category_code': category_code,
                  'category_description': category_description}
        if category_id == '':
            category_obj = Category(**kwargs)
        else:
            category_obj = Category(id=category_id,**kwargs)
        category_obj.save()
        context['success'] = 1

    context['categories'] = Category.objects.all().order_by("category_name")
    template = loader.get_template('app/mydir/categoryentry.html')
    return HttpResponse(template.render(context, request))


def getcategories(request):
    category = request.GET.getlist('metalist[]')[0]
    data = Category.objects.filter(category_name=category)
    if len(data) == 0:
        kwargs = {'category_name': category,
                  'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
        data = Category.objects.filter(**kwargs)
    data = data.values()[0]
    data = "{ 'category': " + str(data) + " }"
    data = ast.literal_eval(data)
    return JsonResponse(data)


@permission_required('app.add_product', login_url='/page_403.html')
def productentry(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['success']=0               # - Indicate successful insertion of category into database
    myfc = Profile.objects.get(user=request.user).franchise_code
    if request.method == 'POST':
        item_id = request.POST.get('item_id', '')
        item_name = request.POST.get('item_name', '')
        short_code = request.POST.get('short_code', '')
        MRP = getInt(request.POST.get('MRP', 0))
        SKU = request.POST.get('SKU', '')
        tax_CGST = getFloat(request.POST.get('tax_cgst', 0))
        tax_SGST = getFloat(request.POST.get('tax_sgst', 0))
        category = request.POST.get('category', '')
        remarks = request.POST.get('remarks', '')
        kwargs = {'item_name': item_name, 'short_code': short_code,
                  'MRP': MRP, 'SKU': SKU, 'tax_SGST': tax_SGST, 'tax_CGST': tax_CGST,
                  'category': category, 'remarks': remarks, 'franchise_code':myfc
                  }
        if item_id == '':
            item_obj = Product(**kwargs)
        else:
            item_obj = Product(id=item_id, **kwargs)
        item_obj.save()
        context['success'] = 1
    context['products'] = Product.objects.filter(franchise_code=0).order_by("item_name") | Product.objects.filter(franchise_code=myfc).order_by("item_name")
    context['category'] = Category.objects.filter(franchise_code=0).order_by("category_name") | Category.objects.filter(franchise_code=myfc).order_by("category_name")
    context['sku'] = SKUList.objects.all()
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/mydir/' + load_template)
    return HttpResponse(template.render(context, request))


@permission_required('app.add_product', login_url='/page_403.html')
def deleteproduct(request):
    del_id = request.GET.getlist('metalist[]')[0]
    data = {}
    obj = Product.objects.filter(id=del_id)
    if len(obj) == 0:
        data['success'] = 0
        data['error'] = "Product not found"
    else:
        obj.delete()
        data['success']=1
    return JsonResponse(data)


def getproducts(request):
    item_name = request.GET.getlist('metalist[]')[0]
    data = Product.objects.filter(item_name=item_name)
    fc = Profile.objects.get(user=request.user).franchise_code
    if len(data) == 0:
        kwargs = {'item_name': item_name,
                  'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
        data = Category.objects.filter(**kwargs)
    data = data.values()[0]
    if data['franchise_code']==fc:
        data['delete'] = 1
    else:
        data['delete'] = 0
    data = "{ 'product': " + str(data) + " }"
    data = ast.literal_eval(data)
    return JsonResponse(data)


def getHOproducts(request):
    item_name = request.GET.getlist('metalist[]')[0]
    fc = Profile.objects.get(user=request.user).franchise_code
    if fc==0:
        data = HOProduct.objects.filter(id=item_name)
    else:
        return JsonResponse()
    data = data.values()[0]
    data = "{ 'product': " + str(data) + " }"
    data = ast.literal_eval(data)
    return JsonResponse(data)


@permission_required('app.add_package', login_url='/page_403.html')
def packageentry(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['success'] = 0  # - Indicate successful insertion of category into database
    if request.method == 'POST':
        package_id = request.POST.get('id', '')
        package_name = request.POST.get('name', '')
        package_code = request.POST.get('code', '')
        rates = ",".join(request.POST.getlist('rates[]', ''))
        remarks = request.POST.get('remarks', '')
        body_part = request.POST.get('bodypart', '')
        description = request.POST.get('description', '')
        try:
            image = request.FILES['image']
        except:
            image = None
        discount = getFloat(request.POST.get('discount', 0))
        tax_CGST = getFloat(request.POST.get('tax_cgst', 0))
        tax_SGST = getFloat(request.POST.get('tax_sgst', 0))
        kwargs = {'name': package_name, 'package_code': package_code, 'body_part':body_part, 'image':image, 'description':description,
                  'remarks': remarks, 'rates': rates, 'discount': discount, 'tax_SGST': tax_SGST, 'tax_CGST': tax_CGST}
        if package_id=="":
            package_obj = Package(**kwargs)
        else:
            package_obj = Package(id=package_id,**kwargs)
        package_obj.save()
        context['success'] = 1
    context['packages'] = Package.objects.all()
    template = loader.get_template('app/mydir/packageentry.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.add_package', login_url='/page_403.html')
def deletepackage(request):
    del_id = request.GET.get('del_id')
    data = {}
    obj = Package.objects.filter(id=int(del_id))
    if len(obj) == 0:
        data['success'] = 0
        data['error'] = "Package not found"
    else:
        obj.delete()
        data['success']=1
    return JsonResponse(data)


def togglepackages(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.method == 'POST':
        packages = Package.objects.all().order_by("id")
        mask = ""
        for p in packages:
            if request.POST.get(str(p.id), '')=='':
                mask+='0'
            else:
                mask+='1'
        myfc= Profile.objects.filter(user=request.user)[0].franchise_code
        kwargs = {'mask':mask,
                  'franchise_code': myfc
                 }
        mymask = PackageMask.objects.filter(franchise_code=myfc)
        if len(mymask) == 0:
            item_obj = PackageMask(**kwargs)
        else:
            item_obj = PackageMask(id=mymask[0].id, **kwargs)
        item_obj.save()
    mymask = PackageMask.objects.filter(franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code)
    if len(mymask) > 0:
        mymask = mymask[0].mask
    else:
        mymask = ''
    context['packages'] = zip(Package.objects.all().order_by("id"), stringtobool(mymask,Package.objects.count()))
    template = loader.get_template('app/mydir/togglepackages.html')
    return HttpResponse(template.render(context, request))


def getpackages(request):
    name = request.GET.getlist('metalist[]')[0]
    data = Package.objects.filter(name=name)
    if len(data) == 0:
        kwargs = {'name': name,
                  'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
        data = Category.objects.filter(**kwargs)
    data = data.values()[0]
    data['rates'] = map(int, data['rates'].split(','))
    data = "{ 'package': " + str(data) + " }"
    data = ast.literal_eval(data)
    return JsonResponse(data)


@permission_required('app.add_service', login_url='/page_403.html')
def serviceentry(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['success']=0               # - Indicate successful insertion of category into database
    if request.method == 'POST':
        service_id = request.POST.get('id', '')
        service_name = request.POST.get('name', '')
        service_code = request.POST.get('code', '')
        rates = ",".join(request.POST.getlist('rates[]', ''))
        remarks = request.POST.get('remarks', '')
        body_part = request.POST.get('bodypart', '')
        description = request.POST.get('description', '')
        try:
            image = request.FILES['image']
        except KeyError:
            image = None
        discount = getFloat(request.POST.get('discount', 0))
        tax_CGST = getFloat(request.POST.get('tax_cgst', 0))
        tax_SGST = getFloat(request.POST.get('tax_sgst', 0))
        kwargs = {'name': service_name, 'service_code': service_code, 'body_part':body_part, 'description':description, 'image':image,
                  'remarks': remarks, 'rates': rates, 'discount': discount, 'tax_SGST': tax_SGST, 'tax_CGST': tax_CGST}
        if service_id=='':
            service_obj = Service(**kwargs)
        else:
            service_obj = Service(id=service_id, **kwargs)
        service_obj.save()
        context['success'] = 1
    context['services']=Service.objects.all()
    template = loader.get_template('app/mydir/serviceentry.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.add_service', login_url='/page_403.html')
def deleteservice(request):
    del_id = request.GET.get('del_id')
    data = {}
    obj = Service.objects.filter(id=int(del_id))
    if len(obj) == 0:
        data['success'] = 0
        data['error'] = "Service not found"
    else:
        obj.delete()
        data['success']=1
    return JsonResponse(data)


def toggleservices(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.method == 'POST':
        services = Service.objects.all().order_by("id")
        mask = ""
        for p in services:
            if request.POST.get(str(p.id), '') == '':
                mask += '0'
            else:
                mask += '1'
        myfc = Profile.objects.filter(user=request.user)[0].franchise_code
        kwargs = {'mask': mask,
                  'franchise_code': myfc
                  }
        mymask = ServiceMask.objects.filter(franchise_code=myfc)
        if len(mymask) == 0:
            item_obj = ServiceMask(**kwargs)
        else:
            item_obj = ServiceMask(id=mymask[0].id, **kwargs)
        item_obj.save()
    mymask = ServiceMask.objects.filter(franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code)
    if len(mymask)>0:
        mymask= mymask[0].mask
    else:
        mymask=''
    context['services'] = zip(Service.objects.all().order_by("id"), stringtobool(mymask,Service.objects.count()))
    template = loader.get_template('app/mydir/toggleservices.html')
    return HttpResponse(template.render(context, request))


def getservices(request):
    name = request.GET.getlist('metalist[]')[0]
    data = Service.objects.filter(name=name)
    if len(data) == 0:
        kwargs = {'name': name,
                  'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
        data = Category.objects.filter(**kwargs)
    data = data.values()[0]
    data['rates'] = map(int, data['rates'].split(','))
    data = "{ 'service': " + str(data) + " }"
    data = ast.literal_eval(data)
    return JsonResponse(data)


@permission_required('app.add_treatment', login_url='/page_403.html')
def treatmententry(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['success']=0               # - Indicate successful insertion of category into database
    if request.method == 'POST':
        treatment_id = request.POST.get('id', '')
        name = request.POST.get('name', '')
        remarks = request.POST.get('remarks', '')
        duration = request.POST.get('duration', '')
        kwargs = {'name': name, 'duration':duration,'remarks': remarks}
        if treatment_id=='':
            treatment_obj = TreatmentMaster(**kwargs)
        else:
            treatment_obj = TreatmentMaster(id=treatment_id, **kwargs)
        treatment_obj.save()
        context['success'] = 1
    context['treatments']=TreatmentMaster.objects.all()
    template = loader.get_template('app/mydir/treatmententry.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.add_treatment', login_url='/page_403.html')
def deletetreatmentmaster(request):
    del_id = request.GET.get('del_id')
    data = {}
    obj = TreatmentMaster.objects.filter(id=int(del_id))
    if len(obj) == 0:
        data['success'] = 0
        data['error'] = "Treatment not found"
    else:
        obj.delete()
        Treatment.objects.filter(id=int(del_id)).delete()
        data['success']=1
    return JsonResponse(data)


def mytreatments(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.method == 'POST':
        treatment_id = request.POST.get('id', '')
        name = request.POST.get('name', '')
        rate = getFloat(request.POST.get('rate', ''))
        tax_cgst = getFloat(request.POST.get('tax_cgst', ''))
        tax_sgst = getFloat(request.POST.get('tax_sgst', ''))
        kwargs = {'name': name, 'rate': rate ,
                  'tax_CGST': tax_cgst,'tax_SGST':tax_sgst,
                  'franchise_code' : Profile.objects.filter(user=request.user)[0].franchise_code}
        if treatment_id == '':
            treatment_obj = Treatment(**kwargs)
        else:
            treatment_obj = Treatment(id=treatment_id, **kwargs)
        treatment_obj.save()
        context['success'] = 1
    context['treatments'] = Treatment.objects.filter(franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code)
    context['treatmentmaster'] = TreatmentMaster.objects.all()
    template = loader.get_template('app/mydir/mytreatments.html')
    return HttpResponse(template.render(context, request))


def deletetreatment(request):
    del_id = request.GET.get('del_id')
    data = {}
    obj = Treatment.objects.filter(id=int(del_id))
    if len(obj) == 0:
        data['success'] = 0
        data['error'] = "Treatment not found"
    else:
        obj.delete()
        data['success']=1
    return JsonResponse(data)


def gettreatments(request):
    name = request.GET.getlist('metalist[]')[0]
    #data = Discount.objects.filter(name=name,franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code)
    #if len(data) == 0:
    kwargs = {'name': name,
              'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
    data = Treatment.objects.filter(**kwargs)
    data = data.values()[0]
    data = "{ 'treatment': " + str(data) + " }"
    data = ast.literal_eval(data)
    return JsonResponse(data)


def gettreatmentmaster(request):
    name = request.GET.getlist('metalist[]')[0]
    #data = Discount.objects.filter(name=name,franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code)
    #if len(data) == 0:
    data = TreatmentMaster.objects.filter(name=name)
    data = data.values()[0]
    data = "{ 'treatment': " + str(data) + " }"
    data = ast.literal_eval(data)
    return JsonResponse(data)

@permission_required('app.price_discount', login_url='/page_403.html')
def discountentry(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['success']=0               # - Indicate successful insertion of category into database
    fcode = Profile.objects.filter(user=request.user)[0].franchise_code
    if request.method == 'POST':
        discount_id = request.POST.get('id', '')
        subject = request.POST.get('subject', '')
        id = getInt(request.POST.get('uid', 0))
        my_map = {'Package': Package, 'Service': Service, 'Product': Product, 'Treatment': Treatment}
        item = my_map[subject].objects.get(id=id)
        type = request.POST.get('type', '')
        value = getFloat(request.POST.get('value', 0))
        if fcode!=0:
            fname = Franchise.objects.get(id=fcode).franchise_name
        else:
            fname = 'Main Office'
        my_map = {'Service': 'sid', 'Package': 'pid', 'Treatment': 'tid', 'Product': 'proid'}
        kwargs = {my_map[subject]:item, 'discount_type': type,'subject':subject,
                  'value': value, 'franchise_code':fcode, 'franchise_name':fname}
        if discount_id=='':
            obj = Discount(**kwargs)
        else:
            obj = Discount(id=discount_id, **kwargs)
        obj.save()
        context['success'] = 1
    context['discounts']=Discount.objects.filter(franchise_code=fcode)
    context['fcode'] = fcode
    template = loader.get_template('app/mydir/discountentry.html')
    return HttpResponse(template.render(context, request))


def getitems(request):
    fcode = Profile.objects.filter(user=request.user)[0].franchise_code
    category_name = request.GET.getlist('metalist[]')[0]
    my_map = {'Package':[Package, PackageMask], 'Service':[Service,ServiceMask], 'Product':Product, 'Treatment':Treatment}
    my_class = my_map[category_name]
    if category_name=="Package" or category_name=="Service":
        data = my_class[0].objects.all()
    elif category_name=="Treatment":
        data = my_class.objects.filter(franchise_code=fcode)
    else:
        data = my_class.objects.filter(franchise_code__in=[0,fcode])
    try:
        data = list(data.values('name','id'))
    except:
        data = list(data.values('item_name','id'))
    data = "{ 'item': " + str(data) + " }"
    data = ast.literal_eval(data)
    return JsonResponse(data)


def getdiscounts(request):
    id = request.GET.getlist('metalist[]')[0]
    data = Discount.objects.filter(id=id)
    data = data.values()[0]
    data = "{ 'discount': " + str(data) + " }"
    data = ast.literal_eval(data)
    return JsonResponse(data)


@permission_required('app.add_stock', login_url='/page_403.html')
def addstock(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    context['success']=0  # - Indicate successful insertion of category into database
    if request.method == 'POST':
        item_name, MRP, pid = Product.objects.filter(id=int(request.POST.get('item_name', ''))).values_list('item_name','MRP','id')[0]
        stock_amount = request.POST.get('stock_amount','')
        batch_no = request.POST.get('batch_no','')
        vendor = request.POST.get('vendor','')
        address = request.POST.get('address','')
        gst_no = request.POST.get('gst_no','')
        hsn_code = request.POST.get('hsn_code','')
        purchase_rate = request.POST.get('purchase_rate','')
        tax_cgst = request.POST.get('tax_cgst','')
        tax_sgst = request.POST.get('tax_sgst','')
        MRP = round(((100.0 + float(tax_cgst) + float(tax_sgst)) / 100.0) * MRP)
        expiry_date = dt.datetime.strptime(request.POST.get('expiry_date', ''), '%d/%m/%Y').date()
        kwargs = {'item_name': item_name, 'stock_quantity': stock_amount, 'batch_no': batch_no, 'vendor': vendor, 'gst_no':gst_no, 'address':address, 'purchase_rate':purchase_rate, 'pid': pid,
                  'expiry_date': expiry_date, 'franchise_code':Profile.objects.filter(user=request.user)[0].franchise_code, 'hsn_code':hsn_code, 'tax_CGST':tax_cgst, 'tax_SGST':tax_sgst, 'MRP':MRP}
        stock_obj = Stock(**kwargs)
        stock_obj.save()
        context['success'] = 1
    fc = Profile.objects.get(user=request.user).franchise_code
    if fc != 0:
        context['list'] = Product.objects.filter(franchise_code__in=[0,fc]).order_by("item_name")
        context['stock'] = Stock.objects.filter(franchise_code=fc)
    else:
        return redirect('newbill')
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/mydir/' + load_template)
    return HttpResponse(template.render(context, request))


@permission_required('app.add_stocktransfer', login_url='/page_403.html')
def stocktransfer(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    myfc = Profile.objects.get(user=request.user).franchise_code
    if request.method == 'POST':
        item_name = request.POST.get('item_name', '')
        id = int(request.POST.get('id', ''))
        if item_name=='':
            context['failure'] = 1
            context['message'] = 'You must select a stock entry'
        reason = request.POST.get('reason', '')
        stock_amount_return = int(request.POST.get('stock_amount_return', 0))
        franchise_name = Franchise.objects.get(id=myfc).franchise_name
        kwargs = {'item_name': item_name, 'stock_quantity_returned': stock_amount_return, 'reason':reason,
                  'franchise_code':myfc, 'franchise_name':franchise_name, 'stock_identifier':id}
        StockReturn(**kwargs).save()
        context['success'] = 1
        context['message'] = 'Successfully submitted stock return request'
    if myfc==0:
        context['requests'] = StockReturn.objects.filter(resolved=False).order_by("franchise_code")
    else:
        context['stock'] = Stock.objects.filter(franchise_code=myfc).order_by("item_name")
    template = loader.get_template('app/mydir/stocktransfer.html')
    return HttpResponse(template.render(context, request))


def getstockdetails(request):
    id = int(request.GET.get('id'))
    data = Stock.objects.filter(id=id)
    data = data.values()[0]
    data.pop('expiry_date')
    data = "{ 'stock': " + str(data) + " }"
    data = ast.literal_eval(data)
    return JsonResponse(data)


def resolvetransferrequest(request):
    id = int(request.GET.get('id'))
    status = request.GET.get('status')
    obj = StockReturn.objects.filter(id=id)
    data={}
    if len(obj)>0:
        obj = obj[0]
        if status == 'Approved':
            obj.approved = True
            stock_obj = Stock.objects.get(id=obj.stock_identifier)
            stock_obj.stock_quantity -= obj.stock_quantity_returned
            stock_obj.stock_quantity = 0 if stock_obj.stock_quantity<0 else stock_obj.stock_quantity
            stock_obj.save()

        obj.resolved = True
        obj.save()
        data['success'] = 1
        data['message'] = status + " request successfully"
    else:
        data['success'] = 0
        data['message'] = "Request not found"
    return JsonResponse(data)

# @permission_required('app.add_skulist', login_url='/page_403.html')
# def skuentry(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['notify']=0
#     if request.method == 'POST':
#         id = request.POST.get('id', '')
#         name = request.POST.get('name', '')
#         unit = request.POST.get('unit', '')
#         franchise_code = Profile.objects.filter(user=request.user)[0].franchise_code
#         kwargs = {'name': name, 'unit': unit,'franchise_code':franchise_code}
#         if id=="":
#             sku_obj = SKUList(**kwargs)
#         else:
#             sku_obj = SKUList(id=id, **kwargs)
#         sku_obj.save()
#         context['notify']=1
#     context['skulist'] = SKUList.objects.all()
#     load_template = request.path.split('/')[-1]
#     template = loader.get_template('app/mydir/' + load_template)
#     return HttpResponse(template.render(context, request))
#
#
# @permission_required('app.add_skulist', login_url='/page_403.html')
# def getskulist(request):
#     unit = request.GET.getlist('metalist[]')[0]
#     data = SKUList.objects.filter(unit=unit)
#     if len(data) == 0:
#         kwargs = {'name': unit,
#                   'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
#         data = SKUList.objects.filter(**kwargs)
#     data = data.values()[0]
#     data = "{ 'sku': " + str(data) + " }"
#     data = ast.literal_eval(data)
#     return JsonResponse(data)
#
#
# def deletesku(request):
#     try:
#         del_id = int(request.GET.getlist('metalist[]')[0])
#     except ValueError:
#         del_id = -1
#     data = {}
#     obj = SKUList.objects.filter(id=del_id)
#     if len(obj) == 0:
#         data['success'] = 0
#         data['error'] = "SKU not found"
#     else:
#         if obj[0].franchise_code == 0 or obj[0].franchise_code == Profile.objects.filter(user=request.user)[0].franchise_code:
#             obj.delete()
#             data['success']=1
#         else:
#             data['success'] = 0
#             data['error'] = "Permission denied"
#     return JsonResponse(data)


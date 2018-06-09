# from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse
# from forms import *
# from models import *
# import pdb
# import datetime
# from django.core.files.base import ContentFile
# from django.core.files.storage import FileSystemStorage
# from django.contrib.auth.models import User, Permission
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required, permission_required
# from django.core.serializers.json import DjangoJSONEncoder
# from django.shortcuts import get_object_or_404
# from django.db.models import Sum
# from django.core.mail import send_mail
# import xlwt, json
# from django.template.defaulttags import register
# import time
# import os
# from django.http import JsonResponse
# import patients
# from Mailing.draft import *
# import ast
# # Create your views here.

from blocks.login import *
from blocks.dasboard import *

from blocks.admin.franchise_management import *
from blocks.admin.inventory_management import *
from blocks.admin.user_management import *

from blocks.reports import *

from blocks.reception import *
from blocks.doctor import *
from blocks.distributor import *
from blocks.billing import *

# @login_required(login_url='login.html')
# def index(request):
#     perm_list={}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename]=True
#     context = {'permissions':perm_list}
#     my_code = Profile.objects.get(user=request.user).franchise_code
#
#     if my_code == 0:
#         context['sales'] = int(round(Franchise.objects.aggregate(Sum('sales_today'))['sales_today__sum']))
#         context['customers'] = int(Franchise.objects.aggregate(Sum('customers_today'))['customers_today__sum'])
#         context['new_customers'] = int(Franchise.objects.aggregate(Sum('new_customers'))['new_customers__sum'])
#         context['enquiries'] = len(Enquiry.objects.filter(timestamp__gte=datetime.datetime.combine(datetime.date.today(),datetime.time.min)))
#     else:
#         context['sales'] = int(round(Franchise.objects.get(id=my_code).sales_today))
#         context['customers'] = int(Franchise.objects.get(id=my_code).customers_today)
#         context['new_customers'] = int(Franchise.objects.get(id=my_code).new_customers)
#         context['enquiries'] = len(Enquiry.objects.filter(timestamp__gte=datetime.datetime.combine(datetime.date.today(), datetime.time.min),franchise_code=my_code))
#     template = loader.get_template('app/mydir/quicknav.html')
#     return HttpResponse(template.render(context, request))


#FRANCHISE FUNCTIONS






#INVENTORY

# @permission_required('app.add_category', login_url='/page_403.html')
# def categoryentry(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['success']=0               # - Indicate successful insertion of category into database
#     if request.method == 'POST':
#         category_id= request.POST.get('category_id', '')
#         category_name = request.POST.get('category_name', '')
#         category_code = request.POST.get('category_code', '')
#         category_description = request.POST.get('category_description', '')
#         discount = getFloat(request.POST.get('discount', 0))
#         tax_CGST = getFloat(request.POST.get('tax_CGST', 0))
#         tax_SGST = getFloat(request.POST.get('tax_SGST', 0))
#         kwargs = {'category_name': category_name, 'category_code': category_code,
#                   'category_description': category_description,
#                   'discount': discount, 'tax_SGST': tax_SGST, 'tax_CGST': tax_CGST}
#         if category_id == '':
#             category_obj = Category(**kwargs)
#         else:
#             category_obj = Category(id=category_id,**kwargs)
#         category_obj.save()
#         context['success'] = 1
#
#     context['categories'] = Category.objects.all().order_by("category_name")
#     template = loader.get_template('app/mydir/categoryentry.html')
#     return HttpResponse(template.render(context, request))
#
#
# def getcategories(request):
#     category = request.GET.getlist('metalist[]')[0]
#     data = Category.objects.filter(category_name=category)
#     if len(data) == 0:
#         kwargs = {'category_name': category,
#                   'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
#         data = Category.objects.filter(**kwargs)
#     data = data.values()[0]
#     data = "{ 'category': " + str(data) + " }"
#     data = ast.literal_eval(data)
#     return JsonResponse(data)
#
#
# @permission_required('app.add_product', login_url='/page_403.html')
# def productentry(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['success']=0               # - Indicate successful insertion of category into database
#     if request.method == 'POST':
#         item_id = request.POST.get('item_id', '')
#         item_name = request.POST.get('item_name', '')
#         short_code = request.POST.get('short_code', '')
#         MRP = getInt(request.POST.get('MRP', 0))
#         SKU = request.POST.get('SKU', '')
#         discount = getFloat(request.POST.get('discount', 0))
#         tax_CGST = getFloat(request.POST.get('tax_CGST', 0))
#         tax_SGST = getFloat(request.POST.get('tax_SGST', 0))
#         category = request.POST.get('category', '')
#         remarks = request.POST.get('remarks', '')
#         kwargs = {'item_name': item_name, 'short_code': short_code,
#                   'MRP': MRP, 'SKU': SKU,'discount': discount, 'tax_SGST': tax_SGST, 'tax_CGST': tax_CGST,
#                   'category': category, 'remarks': remarks, 'franchise_code':0
#                   }
#         if item_id == '':
#             item_obj = Product(**kwargs)
#         else:
#             item_obj = Product(id=item_id, **kwargs)
#         item_obj.save()
#         context['success'] = 1
#     context['products'] = Product.objects.all().order_by("item_name")
#     context['category'] = Category.objects.all().order_by("category_name")
#     context['sku'] = SKUList.objects.all()
#     load_template = request.path.split('/')[-1]
#     template = loader.get_template('app/mydir/' + load_template)
#     return HttpResponse(template.render(context, request))
#
#
# def deleteproduct(request):
#     del_id = request.GET.getlist('metalist[]')[0]
#     data = {}
#     obj = Product.objects.filter(id=del_id)
#     if len(obj) == 0:
#         data['success'] = 0
#         data['error'] = "Product not found"
#     else:
#         obj.delete()
#         data['success']=1
#     return JsonResponse(data)
#
#
# def getproducts(request):
#     item_name = request.GET.getlist('metalist[]')[0]
#     fc = Profile.objects.get(user=request.user).franchise_code
#     if fc==0:
#         data = HOProduct.objects.filter(id=item_name)
#     else:
#         data = Product.objects.filter(item_name=item_name)
#         if len(data) == 0:
#             kwargs = {'item_name': item_name,
#                       'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
#             data = Category.objects.filter(**kwargs)
#     data = data.values()[0]
#     data = "{ 'product': " + str(data) + " }"
#     data = ast.literal_eval(data)
#     return JsonResponse(data)
#
#
# @permission_required('app.add_package', login_url='/page_403.html')
# def packageentry(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['success'] = 0  # - Indicate successful insertion of category into database
#     if request.method == 'POST':
#         package_id = request.POST.get('id', '')
#         package_name = request.POST.get('name', '')
#         package_code = request.POST.get('code', '')
#         rates = ",".join(request.POST.getlist('rates[]', ''))
#         remarks = request.POST.get('remarks', '')
#         body_part = request.POST.get('bodypart', '')
#         description = request.POST.get('description', '')
#         try:
#             image = request.FILES['image']
#         except:
#             image = None
#         discount = getFloat(request.POST.get('discount', 0))
#         tax_CGST = getFloat(request.POST.get('tax_CGST', 0))
#         tax_SGST = getFloat(request.POST.get('tax_SGST', 0))
#         kwargs = {'name': package_name, 'package_code': package_code, 'body_part':body_part, 'image':image, 'description':description,
#                   'remarks': remarks, 'rates': rates, 'discount': discount, 'tax_SGST': tax_SGST, 'tax_CGST': tax_CGST}
#         if package_id=="":
#             package_obj = Package(**kwargs)
#         else:
#             package_obj = Package(id=package_id,**kwargs)
#         package_obj.save()
#         context['success'] = 1
#     context['packages'] = Package.objects.all()
#     template = loader.get_template('app/mydir/packageentry.html')
#     return HttpResponse(template.render(context, request))
#
#
# def togglepackages(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     if request.method == 'POST':
#         packages = Package.objects.all().order_by("id")
#         mask = ""
#         for p in packages:
#             if request.POST.get(str(p.id), '')=='':
#                 mask+='0'
#             else:
#                 mask+='1'
#         myfc= Profile.objects.filter(user=request.user)[0].franchise_code
#         kwargs = {'mask':mask,
#                   'franchise_code': myfc
#                  }
#         mymask = PackageMask.objects.filter(franchise_code=myfc)
#         if len(mymask) == 0:
#             item_obj = PackageMask(**kwargs)
#         else:
#             item_obj = PackageMask(id=mymask[0].id, **kwargs)
#         item_obj.save()
#     mymask = PackageMask.objects.filter(franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code)
#     if len(mymask) > 0:
#         mymask = mymask[0].mask
#     else:
#         mymask = ''
#     context['packages'] = zip(Package.objects.all().order_by("id"), stringtobool(mymask,Package.objects.count()))
#     template = loader.get_template('app/mydir/togglepackages.html')
#     return HttpResponse(template.render(context, request))
#
#
# def getpackages(request):
#     name = request.GET.getlist('metalist[]')[0]
#     data = Package.objects.filter(name=name)
#     if len(data) == 0:
#         kwargs = {'name': name,
#                   'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
#         data = Category.objects.filter(**kwargs)
#     data = data.values()[0]
#     data['rates'] = map(int, data['rates'].split(','))
#     data = "{ 'package': " + str(data) + " }"
#     data = ast.literal_eval(data)
#     return JsonResponse(data)
#
#
# @permission_required('app.add_service', login_url='/page_403.html')
# def serviceentry(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['success']=0               # - Indicate successful insertion of category into database
#     if request.method == 'POST':
#         service_id = request.POST.get('id', '')
#         service_name = request.POST.get('name', '')
#         service_code = request.POST.get('code', '')
#         rates = ",".join(request.POST.getlist('rates[]', ''))
#         remarks = request.POST.get('remarks', '')
#         body_part = request.POST.get('bodypart', '')
#         description = request.POST.get('description', '')
#         try:
#             image = request.FILES['image']
#         except KeyError:
#             image = None
#         discount = getFloat(request.POST.get('discount', 0))
#         tax_CGST = getFloat(request.POST.get('tax_CGST', 0))
#         tax_SGST = getFloat(request.POST.get('tax_SGST', 0))
#         kwargs = {'name': service_name, 'service_code': service_code, 'body_part':body_part, 'description':description, 'image':image,
#                   'remarks': remarks, 'rates': rates, 'discount': discount, 'tax_SGST': tax_SGST, 'tax_CGST': tax_CGST}
#         if service_id=='':
#             service_obj = Service(**kwargs)
#         else:
#             service_obj = Service(id=service_id, **kwargs)
#         service_obj.save()
#         context['success'] = 1
#     context['services']=Service.objects.all()
#     template = loader.get_template('app/mydir/serviceentry.html')
#     return HttpResponse(template.render(context, request))
#
#
# def toggleservices(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     if request.method == 'POST':
#         services = Service.objects.all().order_by("id")
#         mask = ""
#         for p in services:
#             if request.POST.get(str(p.id), '') == '':
#                 mask += '0'
#             else:
#                 mask += '1'
#         myfc = Profile.objects.filter(user=request.user)[0].franchise_code
#         kwargs = {'mask': mask,
#                   'franchise_code': myfc
#                   }
#         mymask = ServiceMask.objects.filter(franchise_code=myfc)
#         if len(mymask) == 0:
#             item_obj = ServiceMask(**kwargs)
#         else:
#             item_obj = ServiceMask(id=mymask[0].id, **kwargs)
#         item_obj.save()
#     mymask = ServiceMask.objects.filter(franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code)
#     if len(mymask)>0:
#         mymask= mymask[0].mask
#     else:
#         mymask=''
#     context['services'] = zip(Service.objects.all().order_by("id"), stringtobool(mymask,Service.objects.count()))
#     template = loader.get_template('app/mydir/toggleservices.html')
#     return HttpResponse(template.render(context, request))
#
#
# def getservices(request):
#     name = request.GET.getlist('metalist[]')[0]
#     data = Service.objects.filter(name=name)
#     if len(data) == 0:
#         kwargs = {'name': name,
#                   'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
#         data = Category.objects.filter(**kwargs)
#     data = data.values()[0]
#     data['rates'] = map(int, data['rates'].split(','))
#     data = "{ 'service': " + str(data) + " }"
#     data = ast.literal_eval(data)
#     return JsonResponse(data)
#
#
# @permission_required('app.add_treatment', login_url='/page_403.html')
# def treatmententry(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['success']=0               # - Indicate successful insertion of category into database
#     if request.method == 'POST':
#         treatment_id = request.POST.get('id', '')
#         name = request.POST.get('name', '')
#         remarks = request.POST.get('remarks', '')
#         body_part = request.POST.get('bodypart', '')
#         duration = request.POST.get('duration', '')
#         kwargs = {'name': name, 'duration':duration, 'body_part':body_part,
#                   'remarks': remarks}
#         if treatment_id=='':
#             treatment_obj = TreatmentMaster(**kwargs)
#         else:
#             treatment_obj = TreatmentMaster(id=treatment_id, **kwargs)
#         treatment_obj.save()
#         context['success'] = 1
#     context['treatments']=TreatmentMaster.objects.all()
#     template = loader.get_template('app/mydir/treatmententry.html')
#     return HttpResponse(template.render(context, request))
#
#
# def mytreatments(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     if request.method == 'POST':
#         treatment_id = request.POST.get('id', '')
#         name = request.POST.get('name', '')
#         rate = getFloat(request.POST.get('rate', ''))
#         tax_cgst = getFloat(request.POST.get('tax_cgst', ''))
#         tax_sgst = getFloat(request.POST.get('tax_sgst', ''))
#         discount = getFloat(request.POST.get('discount', ''))
#         kwargs = {'name': name, 'rate': rate , 'discount': discount,
#                   'tax_CGST': tax_cgst,'tax_SGST':tax_sgst,
#                   'franchise_code' : Profile.objects.filter(user=request.user)[0].franchise_code}
#         if treatment_id == '':
#             treatment_obj = Treatment(**kwargs)
#         else:
#             treatment_obj = Treatment(id=treatment_id, **kwargs)
#         treatment_obj.save()
#         context['success'] = 1
#     context['treatments'] = Treatment.objects.filter(franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code)
#     context['treatmentmaster'] = TreatmentMaster.objects.all()
#     template = loader.get_template('app/mydir/mytreatments.html')
#     return HttpResponse(template.render(context, request))
#
#
# def gettreatments(request):
#     name = request.GET.getlist('metalist[]')[0]
#     #data = Discount.objects.filter(name=name,franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code)
#     #if len(data) == 0:
#     kwargs = {'name': name,
#               'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
#     data = Treatment.objects.filter(**kwargs)
#     data = data.values()[0]
#     data = "{ 'treatment': " + str(data) + " }"
#     data = ast.literal_eval(data)
#     return JsonResponse(data)
#
#
# def gettreatmentmaster(request):
#     name = request.GET.getlist('metalist[]')[0]
#     #data = Discount.objects.filter(name=name,franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code)
#     #if len(data) == 0:
#     data = TreatmentMaster.objects.filter(name=name)
#     #pdb.set_trace()
#     data = data.values()[0]
#     data = "{ 'treatment': " + str(data) + " }"
#     data = ast.literal_eval(data)
#     return JsonResponse(data)
#
# @permission_required('app.price_discount', login_url='/page_403.html')
# def discountentry(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['success']=0               # - Indicate successful insertion of category into database
#     fcode = Profile.objects.filter(user=request.user)[0].franchise_code
#     if request.method == 'POST':
#         discount_id = request.POST.get('id', '')
#         subject = request.POST.get('subject', '')
#         id = getInt(request.POST.get('uid', 0))
#         my_map = {'Package': Package, 'Service': Service, 'Product': Product, 'Additional Procedure': Treatment}
#         item = my_map[subject].objects.get(id=id)
#         type = request.POST.get('type', '')
#         value = getFloat(request.POST.get('value', 0))
#         if fcode!=0:
#             fname = Franchise.objects.get(id=fcode).franchise_name
#         else:
#             fname = 'Head Office'
#         # pdb.set_trace()
#         my_map = {'Service': 'sid', 'Package': 'pid', 'Treatment': 'tid', 'Product': 'proid'}
#         kwargs = {my_map[subject]:item, 'discount_type': type,'subject':subject,
#                   'value': value, 'franchise_code':fcode, 'franchise_name':fname}
#         if discount_id=='':
#             obj = Discount(**kwargs)
#         else:
#             obj = Discount(id=discount_id, **kwargs)
#         obj.save()
#         context['success'] = 1
#     context['discounts']=Discount.objects.filter(franchise_code=fcode)
#     context['fcode'] = fcode
#     template = loader.get_template('app/mydir/discountentry.html')
#     return HttpResponse(template.render(context, request))
#
#
# def getitems(request):
#     fcode = Profile.objects.filter(user=request.user)[0].franchise_code
#     category_name = request.GET.getlist('metalist[]')[0]
#     my_map = {'Package':[Package, PackageMask], 'Service':[Service,ServiceMask], 'Product':Product, 'Additional Procedure':Treatment}
#     my_class = my_map[category_name]
#     if category_name=="Package" or category_name=="Service":
#         data = my_class[0].objects.all()
#     elif category_name=="Additional Procedure":
#         data = my_class.objects.filter(franchise_code=fcode)
#     else:
#         data = my_class.objects.filter(franchise_code=fcode) | my_class.objects.filter(franchise_code=0)
#     try:
#         data = list(data.values('name','id'))
#     except:
#         data = list(data.values('item_name','id'))
#     # pdb.set_trace()
#     data = "{ 'item': " + str(data) + " }"
#     data = ast.literal_eval(data)
#     return JsonResponse(data)
#
#
# def getdiscounts(request):
#     id = request.GET.getlist('metalist[]')[0]
#     data = Discount.objects.filter(id=id)
#     data = data.values()[0]
#     data = "{ 'discount': " + str(data) + " }"
#     data = ast.literal_eval(data)
#     return JsonResponse(data)
#
#
# @permission_required('app.add_stock', login_url='/page_403.html')
# def addstock(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['success']=0  # - Indicate successful insertion of category into database
#     if request.method == 'POST':
#         form=StockForm(request.POST)
#         if form.is_valid():
#             item_name = request.POST.get('item_name', '')
#             stock_amount = request.POST.get('stock_amount','')
#             batch_no = request.POST.get('batch_no','')
#             discount = getInt(request.POST.get('discount', 0))
#             expiry_date = datetime.datetime.strptime(request.POST.get('expiry_date', ''), '%d/%m/%Y').date()
#             kwargs = {'item_name': item_name, 'stock_amount': stock_amount, 'discount': discount, 'batch_no': batch_no,
#                       'expiry_date': expiry_date, 'franchise_code':Profile.objects.filter(user=request.user)[0].franchise_code}
#             stock_obj = Stock(**kwargs)
#             stock_obj.save()
#             context['success'] = 1
#     context['list']= Product.objects.all().order_by("item_name")
#     load_template = request.path.split('/')[-1]
#     template = loader.get_template('app/mydir/' + load_template)
#     return HttpResponse(template.render(context, request))
#
#
# @permission_required('app.add_stocktransfer', login_url='/page_403.html')
# def stocktransfer(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['success']=0  # - Indicate successful insertion of category into database
#     if request.method == 'POST':
#         form = StockTransferForm(request.POST)
#         if form.is_valid():
#             item_name = request.POST.get('item_name', '')
#             stock_amount = request.POST.get('stock_amount', '')
#             franchise_name = request.POST.get('franchise_name', '')
#             discount = getInt(request.POST.get('discount', 0))
#             expiry_date = map(int, request.POST.get('expiry_date').split("/"))
#             expiry_date = datetime.date(expiry_date[2], expiry_date[1], expiry_date[0])
#             kwargs = {'item_name': item_name, 'stock_amount': stock_amount, 'discount': discount,
#                       'franchise_name':franchise_name, 'expiry_date': expiry_date}
#             st_obj = StockTransfer(**kwargs)
#             st_obj.save()
#             context['success'] = 1
#     context['list'] = Product.objects.all().order_by("item_name")
#     context['flist'] = Franchise.objects.all().order_by("franchise_name")
#     load_template = request.path.split('/')[-1]
#     template = loader.get_template('app/mydir/' + load_template)
#     return HttpResponse(template.render(context, request))
#
#
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
#         kwargs = {'name': name, 'unit': unit}
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
#         kwargs = {'name': name,
#                   'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
#         data = SKUList.objects.filter(**kwargs)
#     data = data.values()[0]
#     data = "{ 'sku': " + str(data) + " }"
#     data = ast.literal_eval(data)
#     return JsonResponse(data)
#

# @login_required(login_url='login.html')
# def reports(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     load_template = request.path.split('/')[-1].split('_')[1].split('.')[0]
#     reportdictionary = {'sales':[SalesReportBase, SalesReport],'audit':[SalesReportBase],'stock':[Stock],'implementation':[Implementation], 'inspection':[Inspection]}
#     filterdictionary = {'sales':'sales_base__franchise_code','audit':'franchise_code','stock':'franchise_code','implementation':'franchise_code', 'inspection':'franchise_code'}
#     orderdictionary = {'sales':'sales_base__date','audit':'date','stock':'item_name','implementation':'date','inspection':'date'}
#     context['table_name'] = load_template
#     context['meta'] = []
#
#     for i, table in enumerate(reportdictionary[load_template]):
#         for x in table._meta.get_fields()[i+1:]:
#             context['meta'].append(x.name.replace('_',' ').title())
#     if load_template=='audit':
#         context['meta'].append('Amount')
#
#     fcode = Profile.objects.filter(user=request.user).get().franchise_code
#     if fcode!=0:
#         context[load_template] = reportdictionary[load_template][-1].objects.filter(**{filterdictionary[load_template]:fcode}).order_by(orderdictionary[load_template])
#     else:
#         if 'distributor' in perm_list:
#             if load_template == 'sales':
#                 context[load_template] = reportdictionary[load_template][-1].objects.filter(sales_base__franchise_code__in=Franchise.objects.filter(distributor__user=request.user).values_list('id')).order_by(orderdictionary[load_template])
#             else:
#                 context[load_template] = reportdictionary[load_template][-1].objects.filter(franchise_code__in=Franchise.objects.filter(distributor__user=request.user).values_list('id')).order_by(orderdictionary[load_template])
#             context['franchise_list'] = Franchise.objects.filter(distributor__user=request.user)
#         else:
#             context[load_template] = reportdictionary[load_template][-1].objects.all().order_by(orderdictionary[load_template])
#             context['franchise_list'] = Franchise.objects.all()
#     if load_template == 'audit':
#         context['audit_exp']=[]
#         for row in context[load_template]:
#             context['audit_exp'].append(SalesReport.objects.filter(sales_base=row).aggregate(Sum('sale_rate'))['sale_rate__sum'])
#         context['audit'] = zip(context['audit'], context['audit_exp'])
#     if request.method == "POST":
#         my_post = dict(request.POST)
#         my_post.pop('csrfmiddlewaretoken')
#         daterange = my_post.pop('date',[''])[0]
#         if daterange!='':
#             date1 = datetime.datetime.strptime(daterange.split(' - ')[0], "%B %d, %Y")
#             date2 = datetime.datetime.strptime(daterange.split(' - ')[1], "%B %d, %Y").replace(hour=23, minute=59)
#             context[load_template] = context[load_template].filter(sales_base__date__gte=date1, sales_base__date__lte=date2)
#         my_post = dict((k, v[0]) for k, v in my_post.iteritems() if v != [''])
#         try:
#             my_post['expiry_date__lte'] = datetime.datetime.strptime(my_post['expiry_date__lte'], "%m/%d/%Y").strftime("%Y-%m-%d")
#         except KeyError:
#             pass
#         try:
#             my_post['stock_amount__lte'] = int(my_post['stock_amount__lte'])
#             my_post['stock_amount__gte'] = int(my_post['stock_amount__gte'])
#         except KeyError:
#             pass
#         context[load_template] = context[load_template].filter(**my_post)
#     if len(context[load_template])>50:
#         context[load_template] = context[load_template][:50]
#         context['overflow'] = 1
#     if load_template=='implementation':
#         context['json'] = json.dumps(list(context[load_template].values_list()), cls=DjangoJSONEncoder)
#     context['product_list'] = Product.objects.all()
#     template = loader.get_template('app/mydir/report.html')
#     return HttpResponse(template.render(context, request))
#
#
# @login_required(login_url='login.html')
# def getreport(request):
#     id = int(request.GET.get('id'))
#     table = request.GET.get('table')
#     if table=="Implementation":
#         data = Implementation.objects.filter(id=id).values()[0]
#         data['date_mou'] = data['date_mou'].strftime("%B %d, %Y")
#         data['inaugration_date'] = data['inaugration_date'].strftime("%B %d, %Y")
#     else:
#         data = Inspection.objects.filter(id=id).values()[0]
#     data['date'] = data['date'].strftime("%B %d, %Y")
#     data['distributor'] = Profile.objects.get(id=data['distributor_id']).name
#     data.pop('distributor_id','')
#     data.pop('id','')
#     data = "{ 'data': "+str(data)+" }"
#     data = ast.literal_eval(data)
#     return JsonResponse(data)
#
#
# @login_required(login_url='login.html')
# def export_report(request):
#     response = HttpResponse(content_type='application/ms-excel')
#     table_name = request.path.split('/')[-1].split('.')[0]
#     response['Content-Disposition'] = 'attachment; filename="'+table_name+'.xls"'
#     reportdictionary = {'sales': [SalesReportBase, SalesReport], 'audit': [SalesReportBase], 'stock': [Stock], 'enquiry':[Enquiry]}
#     filterdictionary = {'sales': 'sales_base__franchise_code', 'audit': 'franchise_code', 'stock': 'franchise_code', 'enquiry': 'franchise_code'}
#     orderdictionary = {'sales': 'sales_base__date', 'audit': 'date', 'stock': 'item_name', 'enquiry': 'timestamp'}
#
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet('Sheet 1')
#     row_num = 0
#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True
#
#     columns = []
#     for i, table in enumerate(reportdictionary[table_name]):
#         for x in table._meta.get_fields()[i+1:]:
#             columns.append(x.name.replace('_',' ').title())
#     if table_name=='audit':
#         columns.append('Amount')
#     if table_name == 'enquiry':
#         columns[11] = 'Service / Package Required'
#         columns[15] = 'Franchise'
#         del columns[8:11]
#
#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num], font_style)
#
#     font_style = xlwt.XFStyle()
#     fcode = Profile.objects.filter(user=request.user).get().franchise_code
#     if fcode != 0:
#         rows = reportdictionary[table_name][-1].objects.filter(
#             **{filterdictionary[table_name]: fcode}).values_list().order_by(orderdictionary[table_name])
#     else:
#         rows = reportdictionary[table_name][-1].objects.all().values_list().order_by(
#             orderdictionary[table_name])
#     if table_name == 'sales':
#         rows_copy=rows
#         rows=[]
#         for i, row in enumerate(rows_copy):
#             my_row = SalesReportBase.objects.filter(id=row[1]).values_list()[0]
#             rows.append(my_row[:1]+my_row[:-1]+row[1:])
#         rows_copy,my_row = None, None
#     if table_name == 'audit':
#         rows_exp = []
#         for row in rows:
#             rows_exp.append(
#                 SalesReport.objects.filter(sales_base=row).aggregate(Sum('sale_rate'))['sale_rate__sum'])
#         rows = rows+rows_exp
#     if table_name == 'enquiry':
#         rows = list(rows)
#         for i in range(0,len(rows)):
#             rows[i] = list(rows[i])
#             if rows[i][12] == 'Package':
#                 rows[i][11] = Package.objects.get(id=int(rows[i][11])).name
#             else:
#                 rows[i][11] = Service.objects.get(id=int(rows[i][11])).name
#             rows[i][15] = Franchise.objects.get(id=int(rows[i][15])).franchise_name
#             del rows[i][8:11]
#
#     for row in rows:
#         row_num += 1
#         for col_num in range(1, len(row)):
#             if type(row[col_num]).__name__ == 'datetime':
#                 ws.write(row_num, col_num - 1, row[col_num].strftime("%Y-%m-%d %H:%M"), font_style)
#             else:
#                 ws.write(row_num, col_num-1, row[col_num], font_style)
#
#     wb.save(response)
#     return response
#
#
# @login_required(login_url='login.html')
# def enquiry_report(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     my_fc = Profile.objects.filter(user=request.user)[0].franchise_code
#     if my_fc==0:
#         if 'distributor' in perm_list:
#             context['enquiry'] = Enquiry.objects.filter(franchise_code__in=Franchise.objects.filter(distributor__user=request.user).values_list('id')).order_by('timestamp')
#             context['franchise_list'] = Franchise.objects.filter(distributor__user=request.user)
#         else:
#             context['enquiry'] = Enquiry.objects.all().order_by('timestamp').order_by('timestamp')
#             context['franchise_list'] = Franchise.objects.all()
#     else:
#         context['enquiry'] = Enquiry.objects.filter(franchise_code=my_fc).order_by('timestamp')
#
#     if request.method == "POST":
#         my_post = dict(request.POST)
#         my_post.pop('csrfmiddlewaretoken')
#         daterange = my_post.pop('date',[''])[0]
#         if daterange!='':
#             date1 = datetime.datetime.strptime(daterange.split(' - ')[0], "%B %d, %Y")
#             date2 = datetime.datetime.strptime(daterange.split(' - ')[1], "%B %d, %Y").replace(hour=23, minute=59)
#             context['enquiry'] = context['enquiry'].filter(timestamp__gte=date1, timestamp__lte=date2)
#         my_post = dict((k, v[0]) for k, v in my_post.iteritems() if v != [''])
#         try:
#             if my_post['service_name']:
#                 context['enquiry'] = context['enquiry'].filter(sid=int(my_post['service_name']))
#                 my_post.pop('service_name')
#         except KeyError:
#             try:
#                 if my_post['package_name']:
#                     context['enquiry'] = context['enquiry'].filter(pid=int(my_post['package_name']))
#                     my_post.pop('package_name')
#             except KeyError:
#                 pass
#         context['enquiry'] = context['enquiry'].filter(**my_post)
#
#     context['enquiry'] = list(context['enquiry'])[:50]
#     for i in range(0,len(context['enquiry'])):
#         context['enquiry'][i].franchise = Franchise.objects.get(id=context['enquiry'][i].franchise_code)
#
#     context['table_name'] = 'enquiry'
#     context['service_list'] = Service.objects.all()
#     context['package_list'] = Package.objects.all()
#     context['franchise_list'] = Franchise.objects.all()
#     template = loader.get_template('app/mydir/enquiry_report.html')
#     return HttpResponse(template.render(context, request))
#



#
# def login_request(request):
#     context, perm_list = {}, {}
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = request.POST.get('username', '')
#             password = request.POST.get('password', '')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request,user)
#                 for x in Permission.objects.filter(user=request.user):
#                     perm_list[x.codename] = True
#                 context = {'permissions': perm_list}
#                 my_code = Profile.objects.get(user=request.user).franchise_code
#
#                 if my_code == 0:
#                     context['sales'] = int(round(Franchise.objects.aggregate(Sum('sales_today'))['sales_today__sum']))
#                     context['customers'] = int(
#                         Franchise.objects.aggregate(Sum('customers_today'))['customers_today__sum'])
#                     context['new_customers'] = int(
#                         Franchise.objects.aggregate(Sum('new_customers'))['new_customers__sum'])
#                     context['enquiries'] = len(Enquiry.objects.filter(
#                         timestamp__gte=datetime.datetime.combine(datetime.date.today(), datetime.time.min)))
#                 else:
#                     context['sales'] = int(round(Franchise.objects.get(id=my_code).sales_today))
#                     context['customers'] = int(Franchise.objects.get(id=my_code).customers_today)
#                     context['new_customers'] = int(Franchise.objects.get(id=my_code).new_customers)
#                     context['enquiries'] = len(Enquiry.objects.filter(
#                         timestamp__gte=datetime.datetime.combine(datetime.date.today(), datetime.time.min),
#                         franchise_code=my_code))
#                 template = loader.get_template('app/mydir/quicknav.html')
#                 return HttpResponse(template.render(context, request))
#     template = loader.get_template('app/mydir/login.html')
#     return HttpResponse(template.render(context, request))
#
# def lostpassword(request):
#     context={}
#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         phoneno = request.POST.get('phoneno', '')
#         email = request.POST.get('emailid', '')
#         q = Profile.objects.filter(phoneno=phoneno) | Profile.objects.filter(user__email=email) | Profile.objects.filter(user__username=username)
#         context['results'] = q
#     template = loader.get_template('app/mydir/lostpassword.html')
#     return HttpResponse(template.render(context, request))
#
# @login_required(login_url='login.html')
# def logout_request(request):
#     logout(request)
#     template = loader.get_template('app/mydir/login.html')
#     return HttpResponse(template.render({}, request))


def nop():
    pass

# # To template different kind of users
# def permission_templates(code):
#     mydict = {}
#     if code==0:
#         mydict['Doctor'] = '''[false,false,false,false,false,
#                                             false,false,false,false,false,false,false,false,
#                                             false,false,false,false,
#                                             false,false,false,false,false,false,
#                                             false,false,
#                                             false,false,true,true,false,false,
#                                             false,false]'''
#         mydict['Pharmacist'] = '''[false,false,false,false,false,
#                                             false,false,false,false,false,false,false,false,
#                                             false,false,false,false,
#                                             false,false,false,false,false,false,
#                                             true,true,
#                                             false,false,false,false,false,true,
#                                             false,false]'''
#         mydict['Receptionist'] = '''[false,false,false,false,false,
#                                             false,false,false,false,false,false,false,false,
#                                             false,false,false,false,
#                                             false,false,false,false,false,false,
#                                             false,false,
#                                             true,true,false,false,false,true,
#                                             false,false]'''
#         mydict['Distributor'] = '''[false,false,false,false,false,
#                                             false,false,false,false,false,false,false,false,
#                                             false,false,false,false,
#                                             true,true,false,false,true,true,
#                                             false,false,
#                                             false,false,false,false,false,false,
#                                             true,true]'''
#         mydict['Accounts'] = '''[false,false,false,false,false,
#                                             false,false,false,false,false,false,false,false,
#                                             false,false,false,false,
#                                             true,true,false,true,true,true,
#                                             false,false,
#                                             false,false,false,false,false,false,
#                                             false,false]'''
#         mydict['Admin'] = '''[true,true,true,true,true,
#                                             true,true,true,true,true,true,true,true,
#                                             true,true,true,true,
#                                             true,true,true,true,true,true,
#                                             true,true,
#                                             true,true,true,true,true,true,
#                                             true,true]'''
#     else:
#         mydict['Doctor'] = '''[false,false,
#                                             false,false,false,false,false,false,false,false,
#                                             false,false,false,false,
#                                             false,false,false,false,false,false,
#                                             false,false,
#                                             false,false,true,true,false,false
#                                             ]'''
#         mydict['Pharmacist'] = '''[false,false,
#                                             false,false,false,false,false,false,false,false,
#                                             false,false,false,false,
#                                             false,false,false,false,false,false,
#                                             true,true,
#                                             false,false,false,false,false,true
#                                             ]'''
#         mydict['Receptionist'] = '''[false,false,
#                                             false,false,false,false,false,false,false,false,
#                                             false,false,false,false,
#                                             false,false,false,false,false,false,
#                                             false,false,
#                                             true,true,false,false,false,true
#                                             ]'''
#         mydict['Distributor'] = '''[false,false,
#                                             false,false,false,false,false,false,false,false,
#                                             false,false,false,false,
#                                             true,true,false,false,true,true,
#                                             false,false,
#                                             false,false,false,false,false,false
#                                             ]'''
#         mydict['Accounts'] = '''[false,false,
#                                             false,false,false,false,false,false,false,false,
#                                             false,false,false,false,
#                                             true,true,false,true,true,true,
#                                             false,false,
#                                             false,false,false,false,false,false
#                                             ]'''
#         mydict['Admin'] = '''[true,true,
#                                             true,true,true,true,true,true,true,true,
#                                             true,true,true,true,
#                                             true,true,true,true,true,true,
#                                             true,true,
#                                             true,true,true,true,true,true
#                                             ]'''
#     return mydict
#
#
#
# @permission_required('app.adduser', login_url='/page_403.html')
# def adduser(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['notify']=0
#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         username = request.POST.get('username', '')
#         emailid = request.POST.get('emailid', '')
#         password = User.objects.make_random_password(length=6)
#         organisation = request.POST.get('organisation','')
#         regid = request.POST.get('regid','0')
#         if organisation == '':
#             organisation = Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0].franchise_name
#         role = request.POST.get('role','')
#         phoneno = request.POST.get('phoneno','')
#         user = User.objects.create_user(username, emailid, password)
#         user.save()
#         if role=='Distributor':
#             organisation = 'Main Office'
#             user.user_permissions.add(Permission.objects.get(codename='distributor'))
#         if organisation!="Main Office":
#             franchise_code = Franchise.objects.filter(franchise_name=organisation).get().id
#         else:
#             franchise_code = 0 #-- 0 SYMBOLISES MAIN OFFICE
#         kwargs = {'user':user, 'name':name, 'role':role, 'organisation':organisation, 'franchise_code':franchise_code, 'regid':regid, 'phoneno':phoneno }
#         profile = Profile(**kwargs)
#         profile.save()
#         if request.POST.get('fr_a', '') == 'on':
#             user.user_permissions.add(Permission.objects.get(codename='add_franchise'))
#         user.user_permissions.add(Permission.objects.get(codename='change_franchise')) if request.POST.get('fr_d', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='delete_franchise')) if request.POST.get('fr_e', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Category'), Permission.objects.get(codename='change_Category'), Permission.objects.get(codename='delete_Category')) if request.POST.get('im_c', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_SKUList'), Permission.objects.get(codename='change_SKUList'), Permission.objects.get(codename='delete_SKUList')) if request.POST.get('im_sku', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Product'), Permission.objects.get(codename='change_Product'), Permission.objects.get(codename='delete_Product')) if request.POST.get('im_pr', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Package'), Permission.objects.get(codename='change_Package'), Permission.objects.get(codename='delete_Package')) if request.POST.get('im_pa', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Service'), Permission.objects.get(codename='change_Service'), Permission.objects.get(codename='delete_Service')) if request.POST.get('im_pa', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Stock'), Permission.objects.get(codename='change_Stock'), Permission.objects.get(codename='delete_Stock')) if request.POST.get('im_sa', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_StockTransfer'), Permission.objects.get(codename='change_StockTransfer'), Permission.objects.get(codename='delete_StockTransfer')) if request.POST.get('im_st', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='itemwise_discount')) if request.POST.get('perm1', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='categorywise_discount')) if request.POST.get('perm2', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='price_discount')) if request.POST.get('perm3', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='percentage_discount')) if request.POST.get('perm4', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_SalesReport'), Permission.objects.get(codename='change_SalesReport'), Permission.objects.get(codename='delete_SalesReport')) if request.POST.get('permr1', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_StockReport'), Permission.objects.get(codename='change_StockReport'), Permission.objects.get(codename='delete_StockReport')) if request.POST.get('permr2', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_AuditReport'), Permission.objects.get(codename='change_AuditReport'), Permission.objects.get(codename='delete_AuditReport')) if request.POST.get('permr5', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='delete_Enquiry')) if request.POST.get('permr6', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='adduser')) if request.POST.get('permu1', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='modifyuser')) if request.POST.get('permu2', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='addbill')) if request.POST.get('permb1','') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='viewbill')) if request.POST.get('permb2', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Appointment'), Permission.objects.get(codename='change_Appointment'), Permission.objects.get(codename='delete_Appointment')) if request.POST.get('permd1','') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Customer'), Permission.objects.get(codename='change_Customer'), Permission.objects.get(codename='delete_Customer')) if request.POST.get('permd6','') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='change_Enquiry')) if request.POST.get('permd5','') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='viewdoctor')) if request.POST.get('permd4', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='viewpatient')) if request.POST.get('permd2', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='prescribe')) if request.POST.get('permd3', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='change_implementation')) if request.POST.get('permdis1', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='change_inspection')) if request.POST.get('permdis2', '') == 'on' else nop()
#         user.save()
#         #Send mail
#         kwargs = {'fail_silently': False, 'html_message': My_HTML_Mail(name, username, role, password,organisation), 'recipient_list': [emailid],
#          'from_email': 'care@clubayurveda.com', 'message': '', 'subject': 'Welcome to Club Ayurveda'}
#         send_mail(**kwargs)
#         context['notify']=1
#     context['flist'] = Franchise.objects.all().order_by("franchise_name")
#     context['perm_template'] = permission_templates(Profile.objects.get(user=request.user).franchise_code)
#     template = loader.get_template('app/mydir/adduser.html')
#     return HttpResponse(template.render(context, request))
#
#
# @permission_required('app.adduser', login_url='/page_403.html')
# def edituser(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['notify']=0
#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         username = request.POST.get('username', '')
#         emailid = request.POST.get('emailid', '')
#         password = User.objects.make_random_password(length=6)
#         organisation = request.POST.get('organisation','')
#         regid = request.POST.get('regid','0')
#         if organisation == '':
#             organisation = Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0].franchise_name
#         role = request.POST.get('role','')
#         phoneno = request.POST.get('phoneno','')
#         user = User.objects.create_user(username, emailid, password)
#         user.save()
#         if role=='Distributor':
#             organisation = 'Main Office'
#             user.user_permissions.add(Permission.objects.get(codename='distributor'))
#         if organisation!="Main Office":
#             franchise_code = Franchise.objects.filter(franchise_name=organisation).get().id
#         else:
#             franchise_code = 0 #-- 0 SYMBOLISES MAIN OFFICE
#         kwargs = {'user':user, 'name':name, 'role':role, 'organisation':organisation, 'franchise_code':franchise_code, 'regid':regid, 'phoneno':phoneno }
#         profile = Profile(**kwargs)
#         profile.save()
#         if request.POST.get('fr_a', '') == 'on':
#             user.user_permissions.add(Permission.objects.get(codename='add_franchise'))
#         user.user_permissions.add(Permission.objects.get(codename='change_franchise')) if request.POST.get('fr_d', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='delete_franchise')) if request.POST.get('fr_e', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Category'), Permission.objects.get(codename='change_Category'), Permission.objects.get(codename='delete_Category')) if request.POST.get('im_c', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_SKUList'), Permission.objects.get(codename='change_SKUList'), Permission.objects.get(codename='delete_SKUList')) if request.POST.get('im_sku', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Product'), Permission.objects.get(codename='change_Product'), Permission.objects.get(codename='delete_Product')) if request.POST.get('im_pr', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Package'), Permission.objects.get(codename='change_Package'), Permission.objects.get(codename='delete_Package')) if request.POST.get('im_pa', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Service'), Permission.objects.get(codename='change_Service'), Permission.objects.get(codename='delete_Service')) if request.POST.get('im_pa', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Stock'), Permission.objects.get(codename='change_Stock'), Permission.objects.get(codename='delete_Stock')) if request.POST.get('im_sa', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_StockTransfer'), Permission.objects.get(codename='change_StockTransfer'), Permission.objects.get(codename='delete_StockTransfer')) if request.POST.get('im_st', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='itemwise_discount')) if request.POST.get('perm1', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='categorywise_discount')) if request.POST.get('perm2', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='price_discount')) if request.POST.get('perm3', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='percentage_discount')) if request.POST.get('perm4', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_SalesReport'), Permission.objects.get(codename='change_SalesReport'), Permission.objects.get(codename='delete_SalesReport')) if request.POST.get('permr1', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_StockReport'), Permission.objects.get(codename='change_StockReport'), Permission.objects.get(codename='delete_StockReport')) if request.POST.get('permr2', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_AuditReport'), Permission.objects.get(codename='change_AuditReport'), Permission.objects.get(codename='delete_AuditReport')) if request.POST.get('permr5', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='adduser')) if request.POST.get('permu1', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='modifyuser')) if request.POST.get('permu2', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='addbill')) if request.POST.get('permb1','') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='viewbill')) if request.POST.get('permb2', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='viewdoctor')) if request.POST.get('permd4', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='viewpatient')) if request.POST.get('permd2', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='prescribe')) if request.POST.get('permd3', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Appointment'), Permission.objects.get(codename='change_Appointment'),Permission.objects.get(codename='delete_Appointment')) if request.POST.get('permd1','') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='add_Customer'), Permission.objects.get(codename='change_Customer'),Permission.objects.get(codename='delete_Customer')) if request.POST.get('permd6','') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='change_implementation')) if request.POST.get('permdis1', '') == 'on' else nop()
#         user.user_permissions.add(Permission.objects.get(codename='change_inspection')) if request.POST.get('permdis2', '') == 'on' else nop()
#         user.save()
#         #Send mail
#         kwargs = {'fail_silently': False, 'html_message': My_HTML_Mail(name, username, role, password,organisation), 'recipient_list': [emailid],
#          'from_email': 'care@clubayurveda.com', 'message': '', 'subject': 'Welcome to Club Ayurveda'}
#         send_mail(**kwargs)
#         context['notify']=1
#     my_code = Profile.objects.get(user=request.user).franchise_code
#     context['u'] = Profile.objects.get(id=request.GET['id'])
#     if not (my_code==0 or my_code==context['u'].franchise_code):
#         context.pop('u')
#     perm_list = {}
#     for x in Permission.objects.filter(user=context['u'].user):
#         perm_list[x.codename] = True
#     context['userpermissions'] = perm_list
#     try:
#         context['fname'] = Franchise.objects.get(id=my_code).franchise_name
#     except:
#         context['fname'] = "Main Office"
#     context['flist'] = Franchise.objects.all().order_by("franchise_name")
#     context['doctor'] = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True]
#     context['operator'] = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False]
#     context['admin'] = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
#     template = loader.get_template('app/mydir/edituser.html')
#     return HttpResponse(template.render(context, request))
#
#
# def checkusername(request):
#     data={}
#     if User.objects.filter(username=request.GET['username']).exists():
#         data['message'] = 'Username already exists'
#         data['colour'] = '#990000'
#     else:
#         data['message'] = 'Valid username'
#         data['colour'] = '#009900'
#     return JsonResponse(data)
#
#
# def viewusers(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     fc = Profile.objects.filter(user=request.user)[0].franchise_code
#     if fc == 0:  #<-- Head Office
#         context['user_list'] = Profile.objects.filter().order_by("franchise_code")
#     else:
#         context['user_list'] = Profile.objects.filter(franchise_code=fc).exclude(user=request.user)
#     template = loader.get_template('app/mydir/viewusers.html')
#     return HttpResponse(template.render(context, request))
#
#
# def suspenduser(request):
#     data = {}
#     try:
#         if request.GET['deluser']:
#             u = User.objects.get(username=request.GET['deluser'])
#             data = {'delete': 1}
#             if Profile.objects.filter(user=u)[0].role=="Doctor":
#                 if Profile.objects.filter(user=request.user)[0].franchise_code=='0':
#                     u.delete()
#                 else:
#                     data = {'delete': 2}
#             else:
#                 u.delete()
#     except:
#         try:
#             if request.GET['sususer']:
#                 u = User.objects.get(username=request.GET['sususer'])
#                 u.is_active = not u.is_active
#                 u.save()
#                 if u.is_active:
#                     kwargs = {'fail_silently': False,
#                               'message': "Your ClubAyurveda account has been reactivated.",
#                               'recipient_list': [u.email],
#                               'from_email': 'care@clubayurveda.com', 'subject': 'ClubAyurveda: Account Reactivation Notification'}
#                 else:
#                     kwargs = {'fail_silently': False,
#                               'message': "Your ClubAyurveda account has been suspended. Please contact Admin for clarification",
#                               'recipient_list': [u.email],
#                               'from_email': 'care@clubayurveda.com',
#                               'subject': 'ClubAyurveda: Account Suspension Notification'}
#                 send_mail(**kwargs)
#                 data = {'suspend': 1}
#         except:
#             pass
#     return JsonResponse(data)


# @login_required(login_url='login.html')
# def resetpassword(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     if request.method == 'POST':
#         oldpassword = request.POST.get('oldpassword', '')
#         password = request.POST.get('password', '')
#         password2 = request.POST.get('password2', '')
#         if request.user.check_password(oldpassword):
#             user = request.user
#             user.set_password(password)
#             user.save()
#             context['success'] = 1
#         else:
#             context['failure'] = 1
#     template = loader.get_template('app/mydir/resetpassword.html')
#     return HttpResponse(template.render(context, request))
#
#
# def mailpassword(request):
#     data = {}
#     if request.GET['username']:
#         u = User.objects.get(username=request.GET['username'])
#         password = User.objects.make_random_password(length=6)
#         u.set_password(password)
#         u.save()
#         kwargs = {'fail_silently': False, 'html_message': My_HTML_Mail_reset(Profile.objects.filter(user=u)[0].name, u.username, password),
#                   'recipient_list': [u.email],
#                   'from_email': 'care@clubayurveda.com', 'message': '', 'subject': 'Reset your password'}
#         send_mail(**kwargs)
#         data = {'success': 1}
#     return JsonResponse(data)


# @login_required(login_url='login.html')
# def registerpatient(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         emailid = request.POST.get('emailid', '')
#         gstno = request.POST.get('gstno', '')
#         company_name = request.POST.get('company_name', '')
#         phoneno = request.POST.get('phoneno', '')
#         phoneno_sec = request.POST.get('phoneno2', '')
#         address = request.POST.get('address1', '')+request.POST.get('address2', '')
#         district = request.POST.get('district', '')
#         state = request.POST.get('state', '')
#         country = request.POST.get('country', '')
#         dob = datetime.datetime.strptime(request.POST.get('dob', ''),'%d/%m/%Y').date()
#         franchise_code = Profile.objects.get(user=request.user).franchise_code
#         kwargs = {'name': name, 'emailid': emailid, 'phoneno': phoneno, 'phoneno_sec':phoneno_sec, 'gstno':gstno,
#                   'company_name':company_name, 'address': address, 'district':district, 'state':state, 'country':country,
#                   'dob':dob, 'franchise_code':franchise_code}
#         cust = Customer(**kwargs)
#         cust.save()
#         prefix = state.split('(')[1].split(')')[0]
#         prefix += Country.objects.filter(district=district)[0].district_code
#         cust.customer_code = prefix+str(cust.id)
#         cust.save()
#         fr = Franchise.objects.get(id=franchise_code)
#         fr.new_customers += 1
#         fr.save()
#         patients.newpatient({'name':name,'pid':cust.customer_code})
#         kwargs = {'fail_silently': False,
#                   'html_message': My_HTML_Mail_patient(name,cust.customer_code),
#                   'recipient_list': [emailid],
#                   'from_email': 'care@clubayurveda.com', 'message': '', 'subject': 'Welcome to Club Ayurveda'}
#         send_mail(**kwargs)
#         context['notify'] = 1
#         context['notify_message'] = 'Patient ID - '+cust.customer_code
#     template = loader.get_template('app/mydir/registerpatient.html')
#     return HttpResponse(template.render(context, request))


# @login_required(login_url='login.html')
# def viewpatients(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['customers']=list(Customer.objects.all())
#     for i in range(0, len(context['customers'])):
#         context['customers'][i].franchise = Franchise.objects.get(id=context['customers'][i].franchise_code)
#     template = loader.get_template('app/mydir/viewpatients.html')
#     return HttpResponse(template.render(context, request))


# @login_required(login_url='login.html')
# def doctor_details(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     fc = Profile.objects.filter(user=request.user)[0].franchise_code
#     if fc == 0:  # <-- Head Office
#         context['doctor_list'] = list(Profile.objects.filter(role='Doctor').order_by("franchise_code"))
#     else:
#         context['doctor_list'] = list(Profile.objects.filter(role='Doctor', franchise_code=fc))
#     for i in range(0,len(context['doctor_list'])):
#         context['doctor_list'][i].franchise = Franchise.objects.get(id=context['doctor_list'][i].franchise_code)
#     template = loader.get_template('app/mydir/doctor_details.html')
#     return HttpResponse(template.render(context, request))


# @login_required(login_url='login.html')
# def prescription(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     if request.method == 'GET':
#        try:
#             context['patientID'] = request.GET['q']
#             f = Customer.objects.get(customer_code=request.GET['q'])
#             context['patientphone'] = f.phoneno
#             context['patientname'] = f.name
#        except:
#            pass
#     if request.method == 'POST':
#         num_med = (len(request.POST)-5)/4
#         data={}
#         data['report'] = request.POST.get('report', '')
#         data['diagnosis'] = request.POST.get('diagnosis', '')
#         data['doctor'] = str(request.user)
#         cfees = request.POST.get('cfees',0)
#         if cfees=='':
#             cfees = 0
#         kwargs = {'customer_code':request.POST.get('ccode', ''), 'customer_name':request.POST.get('name', ''), 'doctor_name':request.user, 'franchise_code':Profile.objects.filter(user=request.user)[0].franchise_code, 'consultation_fees':cfees}
#         med_data={}
#         tr_data={}
#         mi,ti=0,0
#         for i in range(1,num_med+1):
#             if request.POST.get('type'+str(i), '')=='Medicine':
#                 med_data[str(mi)]=[]
#                 med_data[str(mi)].append(request.POST.get('type'+str(i), ''))
#                 med_data[str(mi)].append(request.POST.get('medicine'+str(i), ''))
#                 med_data[str(mi)].append(request.POST.get('quantity'+str(i), ''))
#                 med_data[str(mi)].append(request.POST.get('dosage'+str(i), ''))
#                 mi+=1
#             else:
#                 tr_data[str(ti)] = []
#                 tr_data[str(ti)].append(request.POST.get('type' + str(i), ''))
#                 tr_data[str(ti)].append(request.POST.get('medicine' + str(i), ''))
#                 tr_data[str(ti)].append(request.POST.get('quantity' + str(i), ''))
#                 tr_data[str(ti)].append(request.POST.get('dosage' + str(i), ''))
#                 ti+=1
#         if ti:
#             pend_tr = PendingTreatment(**kwargs)
#             pend_tr.save()
#             kwargs.pop('consultation_fees',None)
#             data['treatment'] = tr_data
#             data['pending_trpr'] = 1
#         if mi:
#             pend_pr = PendingPrescription(**kwargs)
#             pend_pr.save()
#             data['prescription'] = med_data
#             data['pending_medpr'] = 1
#         data = {time.strftime("%d %B, %Y") + " :: "+ time.strftime("%H:%M"): data}
#         patients.insertprescription(request.POST.get('ccode', ''),data)
#         context['notify'] = 1
#     template = loader.get_template('app/mydir/prescription_new.html')
#     context['medicine'] = Product.objects.all().order_by("item_name")
#     return HttpResponse(template.render(context, request))


# def getlist(request):
#     data={}
#     if request.GET['meta']=='Package':
#         data['services'] = Package.objects.all().order_by("name").values_list("name", flat=True)
#     elif request.GET['meta']=='Service':
#         data['services'] = Service.objects.all().order_by("name").values_list("name", flat=True)
#     elif request.GET['meta']=='Treatment':
#         data['services'] = Treatment.objects.all().order_by("name").values_list("name", flat=True)
#     else:
#         data['services'] = Product.objects.all().order_by("item_name").values_list("item_name", flat=True)
#     data['services'] = list(data['services'])
#     return JsonResponse(data)
#
#
# def checkstock(request):
#     try:
#         if request.GET['batch_no']:
#             st = Stock.objects.filter(batch_no=request.GET['batch_no'],item_name=request.GET['item'].strip(),franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code)
#     except:
#         st = Stock.objects.filter(item_name=request.GET['item'].strip(),franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code).order_by('expiry_date')
#     batchesq = st.values('batch_no')
#     edq = st.values('expiry_date')
#     countq = st.values('stock_amount')
#     batches, ed, counts=[],[],[]
#     for q in batchesq:
#         batches.append(q['batch_no'])
#     for q in edq:
#         ed.append(datetime.datetime.strftime(q['expiry_date'],"%d/%m/%Y"))
#     for q in countq:
#         counts.append(q['stock_amount'])
#     if len(st)>0:
#         if st[0].stock_amount>0:
#             data = {'success': 1,'item':request.GET['item'],'counts':counts, 'batches':batches, 'ed':ed}
#     else:
#         data = {'success': 0,'item':request.GET['item']}
#     print data
#     return JsonResponse(data)

# @login_required(login_url='login.html')
# def prescriptions_made(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['prescriptionlist'] = PendingPrescription.objects.all().order_by("doctor_name")
#     template = loader.get_template('app/mydir/prescriptionsmade.html')
#     return HttpResponse(template.render(context, request))
#
# @login_required(login_url='login.html')
# def edit_prescription(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     if request.method == 'GET':
#         id = request.GET['id']
#         context['patientID'] = id
#         f = Customer.objects.get(customer_code=id)
#         context['patientphone'] = f.phoneno
#         context['patientname'] = f.name
#         file_data = patients.getdetails(id)
#         for key in file_data.keys():
#             if file_data[key]['pending'] == 1:
#                 pre_details = file_data[key]
#                 context['details'] = pre_details
#                 break
#         context['medicine'] = Product.objects.all().order_by("item_name")
#         context['packages'] = Package.objects.all().order_by("name")
#         context['services'] = Service.objects.all().order_by("name")
#         context['treatments'] = Treatment.objects.all().order_by("name")
#         template = loader.get_template('app/mydir/editprescription.html')
#     elif request.method == 'POST':
#         num_med = (len(request.POST) - 4) / 4
#         data = {}
#         file_data = patients.getdetails(request.POST.get('ccode', ''))
#         for key in file_data.keys():
#             if file_data[key]['pending'] == 1:
#                 patients.deletekey(request.POST.get('ccode', ''),key)
#                 break
#         data['report'] = request.POST.get('report', '')
#         data['diagnosis'] = request.POST.get('diagnosis', '')
#         data['pending'] = 1
#         data['doctor'] = str(request.user)
#         kwargs = {'customer_code': request.POST.get('ccode', ''), 'customer_name': request.POST.get('name', ''),
#                   'doctor_name': str(request.user),
#                   'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code}
#         PendingPrescription.objects.filter(customer_code=request.POST.get('ccode', '')).update(**kwargs)
#         med_data = {}
#         for i in range(1, num_med + 1):
#             med_data[str(i - 1)] = []
#             med_data[str(i - 1)].append(request.POST.get('type' + str(i), ''))
#             med_data[str(i - 1)].append(request.POST.get('medicine' + str(i), ''))
#             med_data[str(i - 1)].append(request.POST.get('quantity' + str(i), ''))
#             med_data[str(i - 1)].append(request.POST.get('dosage' + str(i), ''))
#         data['prescription'] = med_data
#         data = {time.strftime("%d %B, %Y") + " :: " + time.strftime("%H:%M"): data}
#         patients.updatekey(request.POST.get('ccode', ''),data)
#         context['notify'] = 1
#         my_code = Profile.objects.get(user=request.user).franchise_code
#
#         if my_code == 0:
#             context['sales'] = int(round(Franchise.objects.aggregate(Sum('sales_today'))['sales_today__sum']))
#             context['customers'] = int(Franchise.objects.aggregate(Sum('customers_today'))['customers_today__sum'])
#             context['new_customers'] = int(Franchise.objects.aggregate(Sum('new_customers'))['new_customers__sum'])
#             context['enquiries'] = len(Enquiry.objects.filter(
#                 timestamp__gte=datetime.datetime.combine(datetime.date.today(), datetime.time.min)))
#         else:
#             context['sales'] = int(round(Franchise.objects.get(id=my_code).sales_today))
#             context['customers'] = int(Franchise.objects.get(id=my_code).customers_today)
#             context['new_customers'] = int(Franchise.objects.get(id=my_code).new_customers)
#             context['enquiries'] = len(Enquiry.objects.filter(
#                 timestamp__gte=datetime.datetime.combine(datetime.date.today(), datetime.time.min),
#                 franchise_code=my_code))
#         template = loader.get_template('app/mydir/quicknav.html')
#     return HttpResponse(template.render(context, request))


# @login_required(login_url='login.html')
# def recepetion(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     my_fc = Profile.objects.filter(user=request.user)[0].franchise_code
#     if request.method == 'GET':
#         try:
#            verify_dict = {}
#            verify_dict['customer_code'] = request.GET['customercode']
#            if request.GET['phoneno'] != '':
#                verify_dict['phoneno'] = request.GET['phoneno']
#            if request.GET['emailid'] != '':
#                verify_dict['emailid'] = request.GET['emailid']
#            if request.GET['dob'] != '':
#                verify_dict['dob'] = datetime.datetime.strptime(request.GET['dob'],'%d/%m/%Y').date()
#            f = Customer.objects.filter(**verify_dict)
#            if len(f)>0 and len(verify_dict)>=3:
#                f=f[0]
#                context['patientID'] = request.GET['customercode']
#                context['patientphone'] = f.phoneno
#                context['patientname'] = f.name
#                context['success'] = True
#                context['message'] = 'Successfully changed patient to your franchise'
#                f.franchise_code = my_fc
#                f.save()
#                if request.GET['e'] == 1:
#                    context['appointment'] = Appointment.objects.filter(
#                        franchise_code=my_fc,
#                        customer_code=request.GET['customercode'])[0]
#            else:
#                context['failure'] = True
#                if len(verify_dict)<3:
#                    context['message'] = 'Atleast two elements have to be filled'
#                else:
#                    context['message'] = 'No matching patient'
#         except KeyError:
#            try:
#                context['patientID'] = request.GET['q']
#                f = Customer.objects.get(customer_code=request.GET['q'])
#                if f.franchise_code != my_fc:
#                    context['notmyfranchise'] = True
#                    context['customercode'] = request.GET['q']
#                else:
#                    context['patientphone'] = f.phoneno
#                    context['patientname'] = f.name
#                    if request.GET['e'] == 1:
#                        context['appointment'] = Appointment.objects.filter(
#                            franchise_code=my_fc,
#                            customer_code=request.GET['q'])[0]
#            except KeyError:
#                pass
#     if request.method == 'POST':
#         ccode = request.POST.get('ccode', '')
#         doctor = request.POST.get('doctor', '')
#         time = request.POST.get('reservation-time', '')
#         customer_name = Customer.objects.filter(customer_code=ccode)[0].name
#         time=time.split(' - ')
#         format = "%m/%d/%Y %I:%M %p"
#         start_time=datetime.datetime.strptime(time[0],format)
#         end_time=datetime.datetime.strptime(time[1],format)
#         kwargs = {'customer_code': request.POST.get('ccode', ''), 'customer_name':customer_name, 'doctor_name': doctor, 'receptionist_name':str(request.user),
#                   'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code,
#                   'start_time':start_time}
#         objs = Appointment.objects.filter(customer_code=ccode)
#         if len(objs)>0:
#             objs.update(**kwargs)
#         else:
#             appointment = Appointment(**kwargs)
#             appointment.save()
#     context['doctor'] = Profile.objects.filter(role='Doctor', franchise_code = my_fc)
#     context['appointments'] = Appointment.objects.filter(franchise_code = my_fc).order_by('start_time')
#     d = datetime.datetime.today()
#     context['date'] =  d.strftime("%m/%d/%Y")
#     template = loader.get_template('app/mydir/reception.html')
#     return HttpResponse(template.render(context, request))
#
#
# @login_required(login_url='login.html')
# def enquiry(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     my_code = Profile.objects.get(user=request.user).franchise_code
#     if my_code=='0':
#         context['enquiries'] = Enquiry.objects.all()
#     else:
#         context['enquiries'] = Enquiry.objects.filter(franchise_code=my_code)
#     template = loader.get_template('app/mydir/enquiry.html')
#     return HttpResponse(template.render(context, request))
#
#
# @login_required(login_url='login.html')
# def changeenquirystatus(request):
#     e_id = request.GET.getlist('metalist[]')[0]
#     status = request.GET.getlist('metalist[]')[1]
#     data = {}
#     obj = Enquiry.objects.filter(id=e_id)
#     if len(obj) == 0:
#         data['success'] = 0
#         data['error'] = "Enquiry not found"
#     else:
#         obj[0].status = status
#         obj[0].confirmed_time = None
#         if status == "Confirmed":
#             time = request.GET.getlist('metalist[]')[2]
#             time = time.split(' - ')
#             time=time[0]
#             format = "%m/%d/%Y %I:%M %p"
#             start_time = datetime.datetime.strptime(time, format)
#             obj[0].confirmed_time = start_time
#             name = obj[0].name
#             time = time[:11]+'at '+time[11:]
#             kwargs = {'fail_silently': False,
#                       'html_message': My_HTML_Mail_enquiry_confirmation(name, time),
#                       'recipient_list': [obj[0].email],
#                       'from_email': 'care@clubayurveda.com', 'message': '', 'subject': 'Club Ayurveda: Appointment Confirmation'}
#             send_mail(**kwargs)
#         obj[0].save()
#         data['success'] = 1
#     return JsonResponse(data)


# @login_required(login_url='login.html')
# def patient_details(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     if request.method == 'GET':
#         try:
#             context['patientID'] = request.GET['q']
#             f = Customer.objects.get(customer_code=request.GET['q'])
#             context['patientphone'] = f.phoneno
#             context['patientname'] = f.name
#             context['patientid'] = f.customer_code
#             context['history'] = patients.getdetails(request.GET['q'])
#         except:
#            pass
#     context['medicine'] = Product.objects.all().order_by("item_name")
#     template = loader.get_template('app/mydir/patient_details.html')
#     return HttpResponse(template.render(context, request))
#
#
# @login_required(login_url='login.html')
# def pending_patients(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     if request.GET.get('delID'):
#         Appointment.objects.filter(customer_code=request.GET.get('delID')).delete()
#     context['appointments'] = Appointment.objects.filter(
#         franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code,
#         doctor_name=request.user).order_by('start_time')
#     template = loader.get_template('app/mydir/pending_patients.html')
#     return HttpResponse(template.render(context, request))


# @login_required(login_url='login.html')
# def newbill(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['franchise_code'] = Profile.objects.get(user=request.user).franchise_code
#     # HO Inventory
#     if request.method == 'POST':
#         id = request.POST.get('id', '')
#         name = request.POST.get('name', '')
#         rate = float(request.POST.get('rate', ''))
#         tax_cgst = float(request.POST.get('tax_cgst', ''))
#         tax_sgst = float(request.POST.get('tax_sgst', ''))
#         stock = int(request.POST.get('stock', 0))
#         sku = request.POST.get('SKU', '')
#         kwargs = {'item_name': name, 'MRP': rate, 'tax_CGST': tax_cgst,'tax_SGST':tax_sgst,
#                   'stock': stock,'SKU':sku}
#         if id!='':
#             obj = HOProduct(id=id, **kwargs)
#         else:
#             obj = HOProduct(**kwargs)
#         obj.save()
#     if context['franchise_code']==0:
#         context['itemlist'] = HOProduct.objects.all().order_by("item_name")
#         context['sku'] = SKUList.objects.all()
#     else:
#         context['categorylist'] = Category.objects.all().order_by("category_name")
#     template = loader.get_template('app/mydir/newbill.html')
#     return HttpResponse(template.render(context, request))
#
#
# def invoicebill(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     template = loader.get_template('app/mydir/invoicebill.html')
#     return HttpResponse(template.render(context, request))
#
#
# def savebill(request):
#     pl = request.GET.getlist('productlist[]')
#     ml = request.GET.getlist('metalist[]')
#     rl = request.GET.getlist('ratelist[]')
#     dl = request.GET.getlist('durationlist[]')
#     c = Customer.objects.filter(customer_code=ml[0])
#     if len(c) == 0:
#         return JsonResponse({'success':0})
#     else:
#         c = c[0]
#         kwargs = {'customer_code': c.customer_code,
#                   'franchise_code': Profile.objects.filter(user=request.user)[0].franchise_code,
#                   'productlist': str(pl),
#                   'durationlist': str(dl),
#                   'ratelist': str(rl)}
#         objs = SavedBill.objects.filter(customer_code=c.customer_code)
#         if len(objs) > 0:
#             objs.update(**kwargs)
#         else:
#             bill = SavedBill(**kwargs)
#             bill.save()
#     return JsonResponse({'success':1})
#
#
# def printinvoice(request):
#     pl = request.GET.getlist('productlist[]')
#     ml = request.GET.getlist('metalist[]')
#     rl = request.GET.getlist('ratelist[]')
#     dl = request.GET.getlist('durationlist[]')
#     c = Customer.objects.filter(customer_code=ml[0])
#     if len(c)==0:
#         c = ''
#     else:
#         c=c[0]
#     f = Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0]
#     meta={'customer':c, 'franchise':f}
#     pro = []
#     for i in range(0, len(pl)):
#         try:
#             discount = Discount.objects.filter(sid__name=pl[i])
#             pro.append({'product': Service.objects.filter(name=pl[i]).get(), 'rate':rl[i], 'quantity':1, 'discount':discount})
#         except:
#             try:
#                 discount = Discount.objects.filter(pid__name=pl[i])
#                 pro.append({'product': Package.objects.filter(name=pl[i]).get(), 'rate':rl[i], 'quantity':1, 'discount':discount})
#             except:
#                 try:
#                     discount = Discount.objects.filter(tid__name=pl[i], franchise_code=meta['franchise'].id)
#                     product = Treatment.objects.filter(name=pl[i], franchise_code=meta['franchise'].id).get()
#                     duration = TreatmentMaster.objects.get(name=product.name).duration
#                     if dl[i]:
#                         rate = round(float(dl[i])/duration)*float(rl[i])
#                     else:
#                         rate = float(rl[i])
#                     pro.append({'product':product , 'rate':rate,'quantity':1, 'discount':discount})
#                 except:
#                     pro.append({'product':wrapper(pl[i],int(rl[i]),0,0), 'rate':rl[i], 'quantity': 1, 'stock':'','discount':[]})
#     filename = User.objects.make_random_password(length=15)
#     meta['filename'] = filename
#     meta['company_flag'] = int(ml[2])
#     if meta['company_flag']:
#         c.company_name = ml[1]
#         c.save()
#     meta['bill_id'] = reportmanager.manage(meta, pro)
#     total = genbill.ibillpdf(meta, pro)
#     f.sales_today += total
#     f.customers_today += 1
#     f.save()
#     SavedBill.objects.filter(customer_code=ml[0]).delete()
#     return JsonResponse({'filename':filename})
#
#
# def getsavedbill(request):
#     id = request.GET.getlist('ID[]')[0].upper()
#     res = Customer.objects.filter(customer_code=id)
#     if len(res) == 1:
#         objs = SavedBill.objects.filter(customer_code=id)
#         if len(objs)>0:
#             ratelist = ast.literal_eval(objs[0].ratelist)
#             productlist = ast.literal_eval(objs[0].productlist)
#             durationlist = ast.literal_eval(objs[0].durationlist)
#             return JsonResponse({'success': 1, 'company_name':res[0].company_name, 'productlist':productlist,'ratelist':ratelist,'durationlist':durationlist})
#         else:
#             return JsonResponse({'success': 1, 'company_name':res[0].company_name})
#     else:
#         return JsonResponse({'success': 0})
#
#
#
# def get_products(request):
#     fr_data = {"Brahmi":0,"Tulsi":1,"Arayaal":2,"Ashoka":3}
#     type = 'service'
#     ind = fr_data[Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0].franchise_type]
#     if request.GET['category'] == "Services":
#         data = list(Service.objects.all().values())
#         for i in range (0,len(data)):
#             data[i]=dict(data[i])
#             if data[i]['rates'] != '':
#                 r = ast.literal_eval(data[i]['rates'])
#                 data[i]['rates'] = r[ind]
#     elif request.GET['category'] == "Packages":
#         data = list(Package.objects.all().values())
#         for i in range (0,len(data)):
#             data[i]=dict(data[i])
#             if data[i]['rates'] != '':
#                 r = ast.literal_eval(data[i]['rates'])
#                 data[i]['rates'] = r[ind]
#     elif request.GET['category'] == "Treatments":
#         data = list(Treatment.objects.filter(franchise_code=Profile.objects.get(user=request.user).franchise_code).values())
#         for i in range (0,len(data)):
#             data[i]=dict(data[i])
#             data[i]['rates'] = data[i]['rate']
#     elif request.GET['category'] == "Miscellaneous":
#         data = [{"item_name":"Consultation Fee", "MRP":100},
#                 {"item_name":"Extra Charges", "MRP":-1},
#                 {"item_name":"Registration Fee", "MRP":-1},
#                 {"item_name":"Bed Charges", "MRP":-1},
#                 {"item_name":"Clinical Support Services", "MRP":-1},
#                 {"item_name":"Consumables", "MRP":-1},
#                 {"item_name":"Foods & Beverages", "MRP":-1},
#                 {"item_name":"Room Rent", "MRP":-1},]
#         type = 'product'
#     else:
#         data = list(Product.objects.filter(category=request.GET['category']).values())
#         type = 'product'
#     data = {'products':data}
#     data["type"] = type
#     return JsonResponse(data)
#
# #To wrap abnormal items such as consultation fees/extra charges
# class wrapper:
#     def __init__(self,item_name,MRP,tax_CGST,tax_SGST):
#         self.MRP=MRP
#         self.tax_CGST=tax_CGST
#         self.tax_SGST=tax_SGST
#         self.item_name=item_name
#         self.discount=0
#
# import genbill, reportmanager
# def printbill(request):
#     pl = request.GET.getlist('productlist[]')
#     ql = request.GET.getlist('quantitylist[]')
#     bcl = request.GET.getlist('batchcodelist[]')
#     ml = request.GET.getlist('metalist[]')
#     rl = request.GET.getlist('ratelist[]')
#     c = Customer.objects.filter(customer_code=ml[0])
#     if len(c)==0:
#         c = ''
#     else:
#         c=c[0]
#     f = Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0]
#     meta={'customer':c, 'franchise':f}
#     pro = []
#     for i in range(0, len(pl)):
#         try:
#             if len(Product.objects.filter(item_name=pl[i]))>0:
#                 if bcl[i]:
#                     stock = Stock.objects.filter(item_name=pl[i], batch_no=bcl[i], franchise_code=meta['franchise'].id)
#                     if len(stock)>0:
#                         stock=stock[0]
#                     elif len(stock)==0:
#                         stock=""
#                 else:
#                     stock = Stock.objects.filter(item_name=pl[i], franchise_code=meta['franchise'].id)
#                     if len(stock) > 0:
#                         stock = stock[0]
#                     elif len(stock)==0:
#                         stock=""
#             discount = Discount.objects.filter(proid__item_name=pl[i], franchise_code=meta['franchise'].id)
#             pro.append({'product':Product.objects.filter(item_name=pl[i]).get(), 'quantity':ql[i], 'stock':stock, 'discount':discount})
#         except:
#             try:
#                 discount = Discount.objects.filter(sid__name=pl[i])
#                 pro.append({'product': Service.objects.filter(name=pl[i]).get(), 'quantity': ql[i], 'discount':discount})
#             except:
#                 try:
#                     discount = Discount.objects.filter(pid__name=pl[i])
#                     pro.append({'product': Package.objects.filter(name=pl[i]).get(), 'quantity': ql[i], 'discount':discount})
#                 except:
#                     pro.append({'product':wrapper(pl[i],int(rl[i]),0,0), 'quantity': 1, 'stock':'', discount:[]})
#     filename = User.objects.make_random_password(length=15)
#     meta['filename'] = filename
#     meta['company_flag'] = int(ml[2])
#     meta['company_name'] = ml[1]
#     if meta['company_flag']:
#         if c!='':
#             c.company_name = ml[1]
#             c.save()
#     meta['bill_id'] = reportmanager.manage(meta, pro)
#     total = genbill.generatepdf(meta, pro)
#     f.sales_today += total
#     f.customers_today += 1
#     f.save()
#     success, status = genbill.managestock(meta, pro)
#     return JsonResponse({'success':success, 'status':status, 'filename':filename})
#
#
# def print_hobill(request):
#     pl = request.GET.getlist('productlist[]')
#     ql = request.GET.getlist('quantitylist[]')
#     ml = request.GET.getlist('metalist[]')
#     rl = request.GET.getlist('ratelist[]')
#     c = Customer.objects.filter(customer_code=ml[0])
#     pro = []
#     meta = {}
#     for i in range(0, len(pl)):
#         pro.append({'product':HOProduct.objects.filter(item_name=pl[i]).get(), 'quantity':ql[i]})
#
#     filename = User.objects.make_random_password(length=15)
#     meta['filename'] = filename
#     meta['company_flag'] = 0
#     meta['bill_id'] = reportmanager.homanage(meta, pro)
#     genbill.hogeneratepdf(meta, pro)
#     success, status = genbill.homanagestock(meta, pro)
#     return JsonResponse({'success':success, 'status':status, 'filename':filename})
#
#
# def search_id(request):
#     id = request.GET.getlist('ID[]')[0].upper()
#     if id.upper()=="SELF":
#         return JsonResponse({'success':2})
#     res = Customer.objects.filter(customer_code=id)
#     if len(res)==1:
#         return JsonResponse({'success':1,'company_name':res[0].company_name})
#     else:
#         return JsonResponse({'success': 0})
#
#
# @login_required(login_url='login.html')
# def pending_prescription(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     context['medprescriptionlist'] = PendingPrescription.objects.filter(franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code).order_by("customer_name")
#     context['trprescriptionlist'] = PendingTreatment.objects.filter(franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code).order_by("customer_name")
#     template = loader.get_template('app/mydir/pendingprescription.html')
#     return HttpResponse(template.render(context, request))
#
#
# def findrate(ratestring, fcode):
#     mapping = {"Brahmi":0,"Tulsi":1,"Arayaal":2,"Ashoka":3}
#     index = mapping[Franchise.objects.filter(id=fcode)[0].franchise_type]
#     return ratestring.split(',')[index]
#
# def get_pending_prescription(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     id = request.GET['q']
#     context['patientID']=id
#     context['suffix'] =request.GET['suffix']
#     if context['suffix']=='medpr':
#         context['cfees'] = PendingPrescription.objects.filter(customer_code=id)[0].consultation_feesp
#         context['link'] = '/newbill.html?'
#     else:
#         context['cfees'] = PendingTreatment.objects.filter(customer_code=id)[0].consultation_fees
#         context['link'] = '/invoicebill.html?'
#     file_data = patients.getdetails(id)
#     for key in file_data.keys():
#         try:
#             if file_data[key]['pending_'+request.GET['suffix']]==1:
#                 pre_details=file_data[key]
#                 pre_details['rates'] = []
#                 if request.GET['suffix']=='medpr':
#                     for key in pre_details['prescription'].keys():
#                             pre_details['rates'].append(Product.objects.filter(item_name=pre_details['prescription'][key][1])[0].MRP)
#                     pre_details.pop('treatment',None)
#                 else:
#                     for key in pre_details['treatment'].keys():
#                         if pre_details['treatment'][key][0]=='Package':
#                             pre_details['rates'].append(findrate(Package.objects.filter(name=pre_details['treatment'][key][1])[0].rates,Profile.objects.filter(user=request.user)[0].franchise_code))
#                         elif pre_details['treatment'][key][0]=='Service':
#                             pre_details['rates'].append(findrate(Service.objects.filter(name=pre_details['treatment'][key][1])[0].rates,Profile.objects.filter(user=request.user)[0].franchise_code))
#                         elif pre_details['treatment'][key][0]=='Treatment':
#                             pre_details['rates'].append(findrate(Treatment.objects.filter(name=pre_details['treatment'][key][1])[0].rates,Profile.objects.filter(user=request.user)[0].franchise_code))
#                     pre_details.pop('prescription',None)
#                     pre_details['prescription'] = pre_details.pop('treatment',None)
#                 context['details'] = pre_details
#                 break
#         except KeyError:
#             pass
#     template = loader.get_template('app/mydir/prescription_pending.html')
#     return HttpResponse(template.render(context, request))
#
#
# import genpre
# def printprescription(request):
#     m = request.GET.getlist('meta[]')
#     pl = request.GET.getlist('productlist[]')
#     ql = request.GET.getlist('quantitylist[]')
#     dl = request.GET.getlist('dosagelist[]')
#     id = m[2]
#     suffix = m[3]
#     c = Customer.objects.filter(customer_code=id)
#     if len(c)==0:
#         c = ''
#     else:
#         c=c[0]
#     f = Franchise.objects.filter(id=Profile.objects.filter(user=request.user)[0].franchise_code)[0]
#     meta={'customer':c, 'franchise':f}
#     file_data = patients.getdetails(id)
#     for key in file_data.keys():
#         try:
#             if file_data[key]['pending_'+suffix]==1:
#                 file_data[key].pop('pending_'+suffix,None)
#                 meta['doctor']=file_data[key]['doctor']
#                 if suffix=='medpr':
#                     pp = PendingPrescription.objects.filter(customer_code=id)[0]
#                     p = Prescription(pending_prescription=pp)
#                     p.save()
#                     meta['id'] = p.id
#                     pdb.set_trace()
#                     pp.delete()
#                 else:
#                     pt = PendingTreatment.objects.filter(customer_code=id)[0]
#                     p = Prescription(pending_treatment=pt)
#                     p.save()
#                     meta['id'] = p.id
#                     pt.delete()
#                 patients.updatekey(id,{key:file_data[key]})
#                 break
#         except KeyError:
#             pass
#     pro = []
#     for i in range(0, len(pl)):
#         try:
#             pro.append({'product': Product.objects.filter(item_name=pl[i])[0], 'quantity': ql[i], 'dosage':dl[i]})
#         except:
#             try:
#                 pro.append({'product': Package.objects.filter(name=pl[i])[0], 'quantity': ql[i], 'dosage': dl[i]})
#             except:
#                 try:
#                     pro.append({'product': Service.objects.filter(name=pl[i])[0], 'quantity': ql[i]})
#                 except:
#                     try:
#                         pro.append({'product': Treatment.objects.filter(name=pl[i],franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code).get(), 'quantity': ql[i]})
#                     except:
#                         print("Prescription Print Error")
#     filename = User.objects.make_random_password(length=15)
#     meta['filename'] = filename
#     genpre.generatepdf(pro,meta)
#     return JsonResponse({'success': 1, 'filename':filename})


# @permission_required('app.distributor', login_url='/page_403.html')
# def implementation(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     if request.method == 'POST':
#         franchise_code = request.POST.get('franchise_code', '')
#         date_mou = request.POST.get('date_mou', '')
#         date_mou = date_mou[6:]+'-'+date_mou[3:5]+'-'+date_mou[0:2]
#         doi = request.POST.get('doi', '')
#         doi = doi[6:]+'-'+doi[3:5]+'-'+doi[0:2]
#         comments = request.POST.get('comments', '')
#         v1 = True if request.POST.get('v1', '') == 'on' else False
#         v2 = True if request.POST.get('v2', '') == 'on' else False
#         v3 = True if request.POST.get('v3', '') == 'on' else False
#         v4 = True if request.POST.get('v4', '') == 'on' else False
#         kwargs = {'franchise_code': franchise_code, 'distributor': Profile.objects.get(user=request.user),
#                   'painting': v1, 'electrification': v2, 'signboard': v3, 'installation_of_required_equipment': v4,
#                   'date_mou':date_mou, 'inaugration_date': doi, 'comments':comments
#                   }
#         implementation = Implementation(**kwargs)
#         implementation.save()
#         meta = {'row':implementation, 'franchise':Franchise.objects.get(id=franchise_code)}
#         filename = User.objects.make_random_password(length=5)
#         meta['filename'] = str(request.user)+'_'+filename
#         genbill.implementationreport(meta)
#         with open('app/static/bill/'+meta['filename']+'.pdf', 'r') as pdf:
#             response = HttpResponse(pdf.read(), content_type='application/pdf')
#             return response
#     context['franchise_list'] = Franchise.objects.filter(distributor__user=request.user)
#     template = loader.get_template('app/mydir/implementation.html')
#     return HttpResponse(template.render(context, request))
#
#
# @permission_required('app.distributor', login_url='/page_403.html')
# def inspection(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     if request.method == 'POST':
#         franchise_code = request.POST.get('franchise_code', '')
#         staff_behaviour = request.POST.get('staff_behaviour', '')
#         v1 = request.POST.get('v1', '')
#         v2 = request.POST.get('v2', '')
#         v3 = request.POST.get('v3', '')
#         v4 = request.POST.get('v4', '')
#         v5 = request.POST.get('v5', '')
#         v6 = request.POST.get('v6', '')
#         v7 = request.POST.get('v7', '')
#         comments = request.POST.get('comments', '')
#         kwargs = {'franchise_code':franchise_code, 'distributor':Profile.objects.get(user=request.user),
#                   'v1':v1, 'v2':v2, 'v3':v3, 'v4':v4,'v5':v5, 'v6':v6, 'v7':v7,
#                   'staff_behaviour':staff_behaviour, 'comments':comments
#                  }
#         inspection = Inspection(**kwargs)
#         inspection.save()
#         meta = {'row': inspection, 'franchise': Franchise.objects.get(id=franchise_code)}
#         filename = User.objects.make_random_password(length=5)
#         meta['filename'] = str(request.user) + '_' + filename
#         genbill.inspectionreport(meta)
#         with open('app/static/bill/' + meta['filename'] + '.pdf', 'r') as pdf:
#             response = HttpResponse(pdf.read(), content_type='application/pdf')
#             return response
#     context['franchise_list'] = Franchise.objects.filter(distributor__user=request.user)
#     template = loader.get_template('app/mydir/inspection.html')
#     return HttpResponse(template.render(context, request))


# @login_required(login_url='login.html')
# def gentella_html(request):
#     perm_list = {}
#     for x in Permission.objects.filter(user=request.user):
#         perm_list[x.codename] = True
#     context = {'permissions': perm_list}
#     load_template = request.path.split('/')[-1]
#     if load_template=='quicknav.html':
#         my_code = Profile.objects.get(user=request.user).franchise_code
#
#         if my_code == 0:
#             context['sales'] = int(round(Franchise.objects.aggregate(Sum('sales_today'))['sales_today__sum']))
#             context['customers'] = int(Franchise.objects.aggregate(Sum('customers_today'))['customers_today__sum'])
#             context['new_customers'] = int(Franchise.objects.aggregate(Sum('new_customers'))['new_customers__sum'])
#             context['enquiries'] = len(Enquiry.objects.filter(
#                 timestamp__gte=datetime.datetime.combine(datetime.date.today(), datetime.time.min)))
#         else:
#             context['sales'] = int(round(Franchise.objects.get(id=my_code).sales_today))
#             context['customers'] = int(Franchise.objects.get(id=my_code).customers_today)
#             context['new_customers'] = int(Franchise.objects.get(id=my_code).new_customers)
#             context['enquiries'] = len(Enquiry.objects.filter(
#                 timestamp__gte=datetime.datetime.combine(datetime.date.today(), datetime.time.min),
#                 franchise_code=my_code))
#     template = loader.get_template('app/mydir/'+load_template)
#     return HttpResponse(template.render(context, request))
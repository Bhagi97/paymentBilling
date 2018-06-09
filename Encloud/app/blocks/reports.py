from django.template import loader
from django.http import HttpResponse
import pdb
import datetime as dt
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum, F, FloatField
from django.forms.models import model_to_dict

import xlwt, json

import app.patients as patients
from app import genbill
from helper import *


def report_decorator(template,perm_list):
    mymap = {'sales':'add_salesreport', 'stock':'add_stockreport', 'audit':'add_auditreport', 'implementation':'change_implementation', 'inspection':'change_inspection', 'receipt':'receiptreport'}
    if perm_list.get(mymap[template],'') == '':
        return False
    else:
        return True


@login_required(login_url='login.html')
def reports(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    load_template = request.path.split('/')[-1].split('_')[1].split('.')[0]
    # Permission Decorator
    if not report_decorator(load_template,perm_list):
        return HttpResponseRedirect("/page_403.html")
    if load_template=='bill':
        context['real_table_name']='bill'
        load_template='audit'
    reportdictionary = {'sales':[SalesReportBase, SalesReport],'audit':[SalesReportBase],'stock':[Stock],'implementation':[Implementation], 'inspection':[Inspection], 'receipt':[Receipt]}
    filterdictionary = {'sales':'sales_base__franchise_code','audit':'franchise_code','stock':'franchise_code','implementation':'franchise_code', 'inspection':'franchise_code', 'receipt':'franchise__id'}
    orderdictionary = {'sales':'-sales_base__date','audit':'-date','stock':'item_name','implementation':'-date','inspection':'-date','receipt':'-date'}
    context['table_name'] = load_template

    context['meta'] = []
    for i, table in enumerate(reportdictionary[load_template]):
        for x in table._meta.get_fields()[i+1:]:
            context['meta'].append(x.name.replace('_',' ').title())
    if load_template=='audit':
        context['meta'].append('Amount')
    try:
        context['meta'].remove('Franchise Code')
    except ValueError:  #Receipt Report
        context['meta'].remove('Franchise')

    fcode = Profile.objects.filter(user=request.user).get().franchise_code
    if fcode!=0:
        context[load_template] = reportdictionary[load_template][-1].objects.filter(**{filterdictionary[load_template]:fcode}).order_by(orderdictionary[load_template])
    else:
        if 'vendor' in perm_list:
            if load_template == 'sales':
                context[load_template] = reportdictionary[load_template][-1].objects.filter(sales_base__franchise_code__in=Franchise.objects.filter(vendor__user=request.user).values_list('id')).order_by(orderdictionary[load_template])
            else:
                context[load_template] = reportdictionary[load_template][-1].objects.filter(franchise_code__in=Franchise.objects.filter(vendor__user=request.user).values_list('id')).order_by(orderdictionary[load_template])
            context['franchise_list'] = Franchise.objects.filter(vendor__user=request.user)
        else:
            context[load_template] = reportdictionary[load_template][-1].objects.all().order_by(orderdictionary[load_template])
            context['franchise_list'] = Franchise.objects.all()

    if request.method == "POST":
        my_post = dict(request.POST)
        my_post.pop('csrfmiddlewaretoken')
        daterange = my_post.pop('date',[''])[0]
        if daterange!='':
            date1 = dt.datetime.strptime(daterange.split(' - ')[0], "%B %d, %Y")
            date2 = dt.datetime.strptime(daterange.split(' - ')[1], "%B %d, %Y").replace(hour=23, minute=59)
            if load_template == 'audit' or 'receipt':
                context[load_template] = context[load_template].filter(date__gte=date1, date__lte=date2)
            else:
                context[load_template] = context[load_template].filter(sales_base__date__gte=date1, sales_base__date__lte=date2)
        my_post = dict((k, v[0]) for k, v in my_post.iteritems() if v != [''])
        try:
            my_post['expiry_date__lte'] = dt.datetime.strptime(my_post['expiry_date__lte'], "%m/%d/%Y").strftime("%Y-%m-%d")
        except KeyError:
            pass
        try:
            my_post['stock_amount__lte'] = int(my_post['stock_amount__lte'])
            my_post['stock_amount__gte'] = int(my_post['stock_amount__gte'])
        except KeyError:
            pass
        context[load_template] = context[load_template].filter(**my_post)

    # Add franchisee name
    if load_template != "receipt": #Foreign Key table - No need
        context['exp'] = []
        for row in context[load_template]:
            # pdb.set_trace()
            rfc = row.sales_base.franchise_code if load_template=='sales' else row.franchise_code
            if rfc==0:
                context['exp'].append("Main Office")
            else:
                context['exp'].append(Franchise.objects.get(id=rfc).franchise_name)
        context[load_template] = zip(context[load_template], context['exp'])

    #Extra processing for Audit Report
    if load_template == 'audit':
        context['audit_exp']=[]
        for row in context[load_template]:
            context['audit_exp'].append(SalesReport.objects.filter(sales_base__id=row[0].id).aggregate(total=Sum(F('sale_rate') * F('quantity'), output_field=FloatField()))['total'])
        context['audit'] = zip(context['audit'], context['audit_exp'])


    if len(context[load_template])>50:
        context[load_template] = context[load_template][:50]
        context['overflow'] = 1
    if load_template=='implementation':
        for i in range(len(context[load_template])):
            context[load_template][i] = list(context[load_template][i])
            context[load_template][i][0] = model_to_dict(context[load_template][i][0])
        context['json'] = json.dumps(context[load_template], cls=DjangoJSONEncoder)
    context['product_list'] = Product.objects.all()
    template = loader.get_template('app/mydir/report.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='login.html')
def getreport(request):
    id = int(request.GET.get('id'))
    table = request.GET.get('table')
    if table=="Implementation":
        data = Implementation.objects.filter(id=id).values()[0]
        data['date_mou'] = data['date_mou'].strftime("%B %d, %Y")
        data['inaugration_date'] = data['inaugration_date'].strftime("%B %d, %Y")
    else:
        data = Inspection.objects.filter(id=id).values()[0]
    data['date'] = data['date'].strftime("%B %d, %Y")
    data['vendor'] = Profile.objects.get(id=data['vendor_id']).name
    data.pop('vendor_id','')
    rid = data.pop('id','')
    data = "{ 'data': "+str(data)+" , 'rid':"+str(rid)+"}"
    data = ast.literal_eval(data)
    return JsonResponse(data)


@login_required(login_url='login.html')
def export_report(request):
    response = HttpResponse(content_type='application/ms-excel')
    table_name = request.path.split('/')[-1].split('.')[0]
    response['Content-Disposition'] = 'attachment; filename="'+table_name+'.xls"'
    reportdictionary = {'sales': [SalesReportBase, SalesReport], 'audit': [SalesReportBase], 'stock': [Stock], 'enquiry':[Enquiry], 'receipt':[Receipt]}
    filterdictionary = {'sales': 'sales_base__franchise_code', 'audit': 'franchise_code', 'stock': 'franchise_code', 'enquiry': 'franchise_code', 'receipt': 'franchise__id'}
    orderdictionary = {'sales': 'sales_base__date', 'audit': 'date', 'stock': 'item_name', 'enquiry': 'timestamp', 'receipt': 'date'}

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sheet 1')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = []
    for i, table in enumerate(reportdictionary[table_name]):
        for x in table._meta.get_fields()[i+1:]:
            columns.append(x.name.replace('_',' ').title())
    if table_name=='audit':
        columns.append('Amount')
        columns = columns[2:]
    elif table_name=='sales':
        columns = columns[2:]
    elif table_name == 'enquiry':
        columns[13] = 'Service / Package / Treatment Required'
        columns[16] = 'Franchisee'
        del columns[8:13]
    elif table_name == 'stock':
        columns = columns[:-1]
        columns[-1] = 'Billing Rate'

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    fcode = Profile.objects.filter(user=request.user).get().franchise_code
    if fcode != 0:
        rows = reportdictionary[table_name][-1].objects.filter(
            **{filterdictionary[table_name]: fcode}).values_list().order_by(orderdictionary[table_name])
    else:
        rows = reportdictionary[table_name][-1].objects.all().values_list().order_by(
            orderdictionary[table_name])
    if table_name == 'sales':
        rows_copy=rows
        rows=[]
        for i, row in enumerate(rows_copy):
            my_row = list(SalesReportBase.objects.filter(id=row[1]).values_list()[0])
            rows.append(my_row+list(row)[2:])
            rows[i][2] = Customer.objects.get(id=rows[i][2]).customer_code if rows[i][2] else None          # Customer code
            rows[i][5] = Franchise.objects.get(id=rows[i][5]).franchise_name + '(' + str(rows[i][5]) + ')'  # Franchisee
    elif table_name == 'audit':
        rows_copy = rows
        rows = []
        for i, row in enumerate(rows_copy):
            my_row = list(SalesReportBase.objects.filter(id=row[0]).values_list()[0])
            rows.append(my_row)
        for i,row in enumerate(rows):
            rows[i][2] = Customer.objects.get(id=rows[i][2]).customer_code if rows[i][2] else None      # Customer code
            rows[i][5] = Franchise.objects.get(id=rows[i][5]).franchise_name+'('+str(rows[i][5])+')'    # Franchisee
            rows[i].append(SalesReport.objects.filter(sales_base__id=row[0]).aggregate(total=Sum(F('sale_rate') * F('quantity'), output_field=FloatField()))['total'])
    elif table_name == 'receipt':
        rows = list(rows)
        for i in range(len(rows)):
            rows[i] = list(rows[i])
            rows[i][3] = Franchise.objects.get(id=rows[i][3]).franchise_name + '(' + str(rows[i][3]) + ')'  # Franchisee
            rows[i][4] = Customer.objects.get(id=rows[i][4]).customer_code if rows[i][4] else None          # Customer code
            rows[i][5] = Profile.objects.get(id=rows[i][5]).user.username                                   # Cashier
            rows[i][10] = SalesReportBase.objects.get(id=rows[i][10]).bill_id if rows[i][10] else None      # Customer code
    elif table_name == 'enquiry':
        rows = list(rows)
        for i in range(0,len(rows)):
            rows[i] = list(rows[i])
            if rows[i][15] == 'Package':
                rows[i][14] = Package.objects.get(id=int(rows[i][11])).name
            elif rows[i][15] == 'Service':
                rows[i][14] = Service.objects.get(id=int(rows[i][9])).name
            elif rows[i][15] == 'Treatment':
                rows[i][14] = TreatmentMaster.objects.get(id=int(rows[i][13])).name
            rows[i][17] = Franchise.objects.get(id=int(rows[i][17])).franchise_name
            del rows[i][9:14]
    elif table_name == 'stock':
        rows=list(rows)
        for i in range(0, len(rows)):
            rows[i] = list(rows[i])
            rows[i]=rows[i][:-1]

    for row in rows:
        row_num += 1
        for col_num in range(1, len(row)):
            if type(row[col_num]).__name__ == 'datetime':
                ws.write(row_num, col_num - 1, row[col_num].strftime("%d-%m-%Y %H:%M"), font_style)
            elif type(row[col_num]).__name__ == 'date':
                ws.write(row_num, col_num - 1, row[col_num].strftime("%d-%m-%Y"), font_style)
            else:
                ws.write(row_num, col_num-1, row[col_num], font_style)

    wb.save(response)
    return response


@permission_required('app.delete_enquiry', login_url='/page_403.html')
def enquiry_report(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    my_fc = Profile.objects.filter(user=request.user)[0].franchise_code
    if my_fc==0:
        if 'vendor' in perm_list:
            context['enquiry'] = Enquiry.objects.filter(franchise_code__in=Franchise.objects.filter(vendor__user=request.user).values_list('id')).order_by('timestamp')
            context['franchise_list'] = Franchise.objects.filter(vendor__user=request.user)
        else:
            context['enquiry'] = Enquiry.objects.all().order_by('timestamp').order_by('timestamp')
            context['franchise_list'] = Franchise.objects.all()
    else:
        context['enquiry'] = Enquiry.objects.filter(franchise_code=my_fc).order_by('timestamp')

    if request.method == "POST":
        my_post = dict(request.POST)
        my_post.pop('csrfmiddlewaretoken')
        daterange = my_post.pop('date',[''])[0]
        if daterange!='':
            date1 = dt.datetime.strptime(daterange.split(' - ')[0], "%B %d, %Y")
            date2 = dt.datetime.strptime(daterange.split(' - ')[1], "%B %d, %Y").replace(hour=23, minute=59)
            context['enquiry'] = context['enquiry'].filter(timestamp__gte=date1, timestamp__lte=date2)
        my_post = dict((k, v[0]) for k, v in my_post.iteritems() if v != [''])
        try:
            if my_post['service_name']:
                context['enquiry'] = context['enquiry'].filter(sid=int(my_post['service_name']))
                my_post.pop('service_name')
        except KeyError:
            try:
                if my_post['package_name']:
                    context['enquiry'] = context['enquiry'].filter(pid=int(my_post['package_name']))
                    my_post.pop('package_name')
            except KeyError:
                pass
        context['enquiry'] = context['enquiry'].filter(**my_post)

    context['enquiry'] = list(context['enquiry'])[:50]
    for i in range(0,len(context['enquiry'])):
        context['enquiry'][i].franchise = Franchise.objects.get(id=context['enquiry'][i].franchise_code)

    context['table_name'] = 'enquiry'
    context['service_list'] = Service.objects.all()
    context['package_list'] = Package.objects.all()
    context['franchise_list'] = Franchise.objects.all()
    template = loader.get_template('app/mydir/enquiry_report.html')
    return HttpResponse(template.render(context, request))


def get_bill(request):
    id = request.GET.get('id')
    data = SalesReport.objects.filter(sales_base__id=id)
    data = list(data.values())
    data = "{ 'items': " + str(data) + " }"
    data = ast.literal_eval(data)
    return JsonResponse(data)


def printreport(request):
    id = request.GET.get('id')
    type = request.GET.get('type')
    type_dict = {'Implementation':Implementation, 'Inspection': Inspection}
    o = type_dict[type].objects.get(id=id)
    franchise = Franchise.objects.get(id=o.franchise_code)
    meta = {'row': o, 'franchise': franchise}
    filename = User.objects.make_random_password(length=10)
    meta['filename'] = str(request.user) + '_' + filename
    if type=='Implementation':
        genbill.implementationreport(meta)
    elif type=='Inspection':
        genbill.inspectionreport(meta)
    data = "{ 'success': 0, 'url':'"+ meta['filename'] +"' }"
    data = ast.literal_eval(data)
    return JsonResponse(data)


@permission_required('app.prescriptionreport', login_url='/page_403.html')
def prescriptionreport(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.method == 'GET':
        try:
            context['patient'] = Customer.objects.get(customer_code=request.GET['q'])
            today = dt.date.today()
            born = context['patient'].dob
            context['patient'].age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            # Range may or may not be in GET dictionary
            try:
                context['history'] = patients.getdetails(request.GET['q'],request.GET['range'])
            except:
                context['history'] = patients.getdetails(request.GET['q'])
        except:
           pass
    template = loader.get_template('app/mydir/prescriptionreport.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.delete_auditreport', login_url='/page_403.html')
def deletebill(request):
    del_id = request.GET.get('del_id')
    data = {}
    obj = SalesReportBase.objects.filter(id=int(del_id))
    if len(obj) == 0:
        data['success'] = 0
        data['error'] = "Bill not found"
    else:
        obj.delete()
        data['success']=1
    return JsonResponse(data)
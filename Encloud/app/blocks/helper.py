from app.models import *
import pdb
import ast
import datetime as dth
from django.http import JsonResponse
from django.template.defaulttags import register

def nop():
    pass

def map_str_to_bool(stringval):
    if stringval=='on':
        return True
    else:
        return False


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def getInt(s):
    if s=='':
        return 0
    else:
        return int(s)


def getFloat(s):
    if s == '':
        return 0
    else:
        return float(s)


def stringtobool(s,len):
    bool_array = []
    for c in s:
        if c=='1':
            bool_array.append(True)
        else:
            bool_array.append(False)
    if s=='':
        return [False] * len
    return bool_array


def getstates(request):
    country = request.GET.getlist('metalist[]')[0]
    data=[]
    for c in Country.objects.filter(country=country):
        data.append(c.state)
    data = list(set(data))
    data.sort()
    data=str(data)
    data = '{ "states": ' + data + ' }'
    data = ast.literal_eval(data)
    return JsonResponse(data)


def getdistricts(request):
    country = request.GET.getlist('metalist[]')[0]
    state = request.GET.getlist('metalist[]')[1]
    data = []
    for c in Country.objects.filter(country=country, state=state):
        data.append(c.district)
    data = list(set(data))
    data.sort()
    data = str(data)
    data = '{ "districts": ' + data + ' }'
    data = ast.literal_eval(data)
    return JsonResponse(data)


def getlist(request):
    data={}
    myfc = Profile.objects.get(user=request.user).franchise_code
    if request.GET['meta']=='Package':
        data['services'] = Package.objects.all().order_by("name").values_list("name", flat=True)
    elif request.GET['meta']=='Service':
        data['services'] = Service.objects.all().order_by("name").values_list("name", flat=True)
    elif request.GET['meta']=='Treatment':
        data['services'] = Treatment.objects.filter(franchise_code=myfc).order_by("name").values_list("name", flat=True)
    else:
        data['services'] = Product.objects.all().order_by("item_name").values_list("item_name", "id")
    data['services'] = list(data['services'])
    return JsonResponse(data)


def checkstock(request):
    try:
        if request.GET['batch_no']:
            st = Stock.objects.filter(batch_no=request.GET['batch_no'],pid=int(request.GET['id']),franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code,stock_quantity__gte=1)
    except KeyError:
        st = Stock.objects.filter(pid=int(request.GET['id']),franchise_code=Profile.objects.filter(user=request.user)[0].franchise_code,stock_quantity__gte=1).order_by('expiry_date')
    batches = map(lambda q: q[0], st.values_list('batch_no') )
    ed = map(lambda q: dth.datetime.strftime(q[0],"%d/%m/%Y") , st.values_list('expiry_date'))
    counts = map(lambda q: q[0] ,st.values_list('stock_quantity'))
    rates = map(lambda q: q[0] ,st.values_list('MRP'))
    hsncodes = map(lambda q: q[0] ,st.values_list('hsn_code'))
    ids = map(lambda q: q[0] ,st.values_list('id'))

    #Discount
    for i,id in enumerate(ids):
        d = Discount.objects.filter(proid__id=st[i].pid)
        if len(d)>0:
            d = d[0]
            product = Product.objects.get(id=st[i].pid)
            new_price = rates[i]-d.value if d.discount_type=="Price" else round(product.MRP*(100-d.value)/100 + (rates[i]-product.MRP))
            rates[i] = str(rates[i])+','+str(new_price)

    data = {'success': 0, 'pid': request.GET['id']}
    if len(st)>0:
        data = {'success': 1,'pid':request.GET['id'], 'rates':rates, 'counts':counts, 'batches':batches, 'hsncodes':hsncodes, 'ed':ed, 'ids':ids}

    return JsonResponse(data)


def roundTime(mydt=None, roundTo=60):
   """Round a datetime object to any time laps in seconds
   dt : datetime.datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   """
   if mydt == None : mydt = dth.datetime.now()
   seconds = (mydt.replace(tzinfo=None) - mydt.min).seconds
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return mydt + dth.timedelta(0,rounding-seconds,-mydt.microsecond)


def customerFranchiseeVerification(request):
    data={}
    my_fc = Profile.objects.get(user=request.user).franchise_code
    if my_fc != 0:
        my_f = Franchise.objects.get(id=my_fc)
    verify_dict = {}
    metalist = request.GET.getlist('metalist[]')
    verify_dict['customer_code'] = metalist[0]
    if metalist[1] != '':
        verify_dict['phoneno'] = metalist[1]
    if metalist[2] != '':
        verify_dict['emailid'] = metalist[2]
    if metalist[3] != '':
        verify_dict['dob'] = dth.datetime.strptime(metalist[3], '%d/%m/%Y').date()
    c = Customer.objects.filter(**verify_dict)
    if len(c) > 0 and len(verify_dict) >= 3:
        c = c[0]
        data['success'] = True
        data['message'] = 'Successfully changed patient to your franchise'
        c.franchise_code = my_fc
        c.save()
    else:
        data['success'] = False
        if len(verify_dict) < 3:
            data['message'] = 'Atleast two elements have to be filled'
        else:
            data['message'] = 'No matching patient'
    return JsonResponse(data)


def get_base_product(request):
    id = request.GET.get('id')
    try:
        data = Product.objects.get(id=int(id)).__dict__
        data.pop('_state')
        data['success'] = 1
    except:
        data = {'success':0}
    return JsonResponse(data)


def get_stock_item(request):
    id = request.GET.get('id')
    try:
        data = Stock.objects.get(id=int(id)).__dict__
        data['expiry_date'] = dth.datetime.strftime(data['expiry_date'],"%d/%m/%Y")
        data.pop('_state')
        data['success'] = 1
    except:
        data = {'success': 0}
    return JsonResponse(data)


def findrate(ratestring, fcode):
    mapping = {"Brahmi":0,"Tulsi":1,"Arayaal":2,"Ashoka":3}
    index = mapping[Franchise.objects.filter(id=fcode)[0].franchise_type]
    return ratestring.split(',')[index]
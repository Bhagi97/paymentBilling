from django.template import loader
from django.http import HttpResponse
import pdb
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import permission_required
from helper import *
import app.genbill as genbill


@permission_required('app.vendor', login_url='/page_403.html')
def implementation(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.method == 'POST':
        franchise_code = request.POST.get('franchise_code', '')
        date_mou = request.POST.get('date_mou', '')
        date_mou = date_mou[6:]+'-'+date_mou[3:5]+'-'+date_mou[0:2]
        doi = request.POST.get('doi', '')
        doi = doi[6:]+'-'+doi[3:5]+'-'+doi[0:2]
        comments = request.POST.get('comments', '')
        v1 = True if request.POST.get('v1', '') == 'on' else False
        v2 = True if request.POST.get('v2', '') == 'on' else False
        v3 = True if request.POST.get('v3', '') == 'on' else False
        v4 = True if request.POST.get('v4', '') == 'on' else False
        kwargs = {'franchise_code': franchise_code, 'vendor': Profile.objects.get(user=request.user),
                  'painting': v1, 'electrification': v2, 'signboard': v3, 'installation_of_required_equipment': v4,
                  'date_mou':date_mou, 'inaugration_date': doi, 'comments':comments
                  }
        implementation = Implementation(**kwargs)
        implementation.save()
        meta = {'row':implementation, 'franchise':Franchise.objects.get(id=franchise_code)}
        filename = User.objects.make_random_password(length=5)
        meta['filename'] = str(request.user)+'_'+filename
        genbill.implementationreport(meta)
        with open('/var/www/html/media/bill/'+meta['filename']+'.pdf', 'r') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            return response
    context['franchise_list'] = Franchise.objects.filter(vendor__user=request.user)
    template = loader.get_template('app/mydir/implementation.html')
    return HttpResponse(template.render(context, request))


@permission_required('app.vendor', login_url='/page_403.html')
def inspection(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    if request.method == 'POST':
        franchise_code = request.POST.get('franchise_code', '')
        staff_behaviour = request.POST.get('staff_behaviour', '')
        v1 = request.POST.get('v1', '')
        v2 = request.POST.get('v2', '')
        v3 = request.POST.get('v3', '')
        v4 = request.POST.get('v4', '')
        v5 = request.POST.get('v5', '')
        v6 = request.POST.get('v6', '')
        v7 = request.POST.get('v7', '')
        comments = request.POST.get('comments', '')
        kwargs = {'franchise_code':franchise_code, 'vendor':Profile.objects.get(user=request.user),
                  'v1':v1, 'v2':v2, 'v3':v3, 'v4':v4,'v5':v5, 'v6':v6, 'v7':v7,
                  'staff_behaviour':staff_behaviour, 'comments':comments
                 }
        inspection = Inspection(**kwargs)
        inspection.save()
        meta = {'row': inspection, 'franchise': Franchise.objects.get(id=franchise_code)}
        filename = User.objects.make_random_password(length=5)
        meta['filename'] = str(request.user) + '_' + filename
        genbill.inspectionreport(meta)
        with open('/var/www/html/media/bill/' + meta['filename'] + '.pdf', 'r') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            return response
    context['franchise_list'] = Franchise.objects.filter(vendor__user=request.user)
    template = loader.get_template('app/mydir/inspection.html')
    return HttpResponse(template.render(context, request))
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.

def index(request):
    return JsonResponse({'foo':'bar'})
    #return HttpResponse('res':"Hello, world. You're at the polls index.")


@csrf_exempt 
def dr_addPrescription(request):
    json_data = json.loads(request.body)   
    idDr = json_data.get('idDr')
    NationalIDPationt = json_data.get('NationalIDPationt')
    drugllist = json_data.get('drugllist')
    comment = json_data.get('comment')
    print(','.join(drugllist))
    a = Prescript(idDr=idDr, NationalIDPationt=NationalIDPationt,drugllist=','.join(drugllist), comment=comment)
    a.save()
    return JsonResponse({"message":"done"})


@csrf_exempt 
def p_listpres(request):
    json_data = json.loads(request.body)   
    id = json_data.get('id')
    a = Prescript.objects.filter(NationalIDPationt=id)
    res = []
    for i in a:
        res.append({
            "idDr":i.idDr,
            "drugllist":i.drugllist.split(','),
            "comment":i.comment
        }
        )
    return JsonResponse({'message':res})

@csrf_exempt 
def admin_getstatistics(request):
    return JsonResponse({
        "totalPrescript":Prescript.objects.count()
    })

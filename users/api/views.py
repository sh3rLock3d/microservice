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
def dr_signin(request):
    json_data = json.loads(request.body)
    name = json_data.get('name')
    nationalCode = json_data.get('nationalCode')
    password = json_data.get('password')

    try:
        dr = Doctor(name=name, nationalCode=nationalCode, password=password)
        dr.save()
    except Exception as e:
        return JsonResponse({'error':str(e)})

    return JsonResponse({'message':dr.id})

@csrf_exempt 
def dr_login(request):    
    json_data = json.loads(request.body)
    nationalCode = json_data.get('nationalCode')
    password = json_data.get('password')
    try:
        a = Doctor.objects.get(nationalCode=nationalCode)
    except Exception as e:
        return JsonResponse({'error':str(e)})
    if a.password != password:
        return JsonResponse({'error':"password is wrong"})
    return JsonResponse({'id':a.id})

@csrf_exempt 
def dr_get_profile(request):
    json_data = json.loads(request.body)
    id = int(json_data.get('id'))
    try:
        a = Doctor.objects.get(id=id)
    except Exception as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse({'name':a.name, "nationalCode":a.nationalCode})

#######################

@csrf_exempt 
def p_signin(request):
    json_data = json.loads(request.body)
    name = json_data.get('name')
    nationalCode = json_data.get('nationalCode')
    password = json_data.get('password')
    try:
        p = Patient(name=name, nationalCode=nationalCode, password=password)
        p.save()
    except Exception as e:
        return JsonResponse({'error':str(e)})

    return JsonResponse({'message':p.id})

@csrf_exempt 
def p_login(request):    
    json_data = json.loads(request.body)
    nationalCode = json_data.get('nationalCode')
    password = json_data.get('password')
    try:
        a = Patient.objects.get(nationalCode=nationalCode)
    except Exception as e:
        return JsonResponse({'error':str(e)})
    if a.password != password:
        return JsonResponse({'error':"password is wrong"})
    return JsonResponse({'id':a.id})


@csrf_exempt 
def p_get_profile(request):    
    json_data = json.loads(request.body)
    id = int(json_data.get('id'))
    try:
        a = Patient.objects.get(id=id)
    except Exception as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse({'name':a.name, "nationalCode":a.nationalCode})


@csrf_exempt 
def admin_login(request):
    json_data = json.loads(request.body)
    password = json_data.get('password')
    if password == "1234":
        return JsonResponse({'id':'1'})
    else:
        return JsonResponse({'error':'password is incorrect'})

@csrf_exempt
def admin_getProfile(request):    
    json_data = json.loads(request.body)
    id = json_data.get('id')
    if id == "1":
        return JsonResponse({"name":"admin", "nationalCode":"a123456789"})
    else:
        return JsonResponse({'error':"id doesn't exist"})

@csrf_exempt
def doExist(request):
    json_data = json.loads(request.body)
    p = json_data.get('p')
    d = json_data.get('d')
    
    try:
        a = Patient.objects.get(nationalCode=p)
    except Exception as e:
        return JsonResponse({'m':False, "error":"patient doesnt exist"})
    
    try:
        a = Doctor.objects.get(id=d)
    except Exception as e:
        return JsonResponse({'m':False, "error":"doctor doesnt exist"})
    
    return JsonResponse({'m':True})

@csrf_exempt
def  stat(request):
    return JsonResponse({
        'totalDr':Doctor.objects.count(),
        "totalPatient":Patient.objects.count()
    })
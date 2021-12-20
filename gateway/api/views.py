from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
USERS = "http://127.0.0.1:8001/"
PRESCRIPT = "http://127.0.0.1:8002/"

def index(request):
    return JsonResponse({'foo':'bar'})
    #return HttpResponse('res':"Hello, world. You're at the polls index.")


# {name, nationalCode, password} return {id}
@csrf_exempt 
def dr_signin(request):
    json_data = json.loads(request.body)   
    if json_data.get('name') == None:
        return JsonResponse({'message':'insert name'})    
    if json_data.get('nationalCode') == None:
        return JsonResponse({'message':'insert nationalCode'})    
    if json_data.get('password') == None:
        return JsonResponse({'message':'insert password'})    
    r = requests.post(USERS + "dr/signin", data=json.dumps(json_data)) 
    a = r.json()
    return JsonResponse(a)

# {nationalCode, password} return {id}
@csrf_exempt 
def dr_login(request):
    json_data = json.loads(request.body)   
    if json_data.get('nationalCode') == None:
        return JsonResponse({'message':'insert nationalCode'})    
    if json_data.get('password') == None:
        return JsonResponse({'message':'insert password'})    
    r = requests.post(USERS + "dr/login", data=json.dumps(json_data)) 
    a = r.json()
    return JsonResponse(a)

# {id} return {name, nationalCode}
@csrf_exempt
def dr_get_profile(request):
    json_data = json.loads(request.body)   
    if json_data.get('id') == None:
        return JsonResponse({'message':'insert id'})    
    r = requests.post(USERS + "dr/get_profile", data=json.dumps(json_data)) 
    a = r.json()
    return JsonResponse(a)

# {idDr, NationalIDPationt, [...drugllist], comment} return {done}
@csrf_exempt
def dr_addPrescription(request):
    # check if pationt exists
    return JsonResponse({'message':'done'})

################

# {name, nationalCode, password} return {id}
@csrf_exempt
def p_signin(request):
    json_data = json.loads(request.body)   
    if json_data.get('name') == None:
        return JsonResponse({'message':'insert name'})    
    if json_data.get('nationalCode') == None:
        return JsonResponse({'message':'insert nationalCode'})    
    if json_data.get('password') == None:
        return JsonResponse({'message':'insert password'})    
    r = requests.post(USERS + "p/signin", data=json.dumps(json_data)) 
    a = r.json()
    return JsonResponse(a)

# {nationalCode, password} return {id}
@csrf_exempt
def p_login(request):
    json_data = json.loads(request.body)   
    if json_data.get('nationalCode') == None:
        return JsonResponse({'message':'insert nationalCode'})    
    if json_data.get('password') == None:
        return JsonResponse({'message':'insert password'})    
    r = requests.post(USERS + "p/login", data=json.dumps(json_data)) 
    a = r.json()
    return JsonResponse(a)

# {id} return {name, nationalCode}
@csrf_exempt
def p_get_profile(request):
    json_data = json.loads(request.body)   
    if json_data.get('id') == None:
        return JsonResponse({'message':'insert id'})    
    r = requests.post(USERS + "p/get_profile", data=json.dumps(json_data)) 
    a = r.json()
    return JsonResponse(a)

# {id} return {[...,list of prescript], [..., list of drs]}
def p_listpres(request):
    return JsonResponse({'message':'done'})

def admin_login(request):
    return JsonResponse({'message':'done'})


def admin_getProfile(request):
    return JsonResponse({'message':'done'})


def admin_getstatistics(request):
    return JsonResponse({'message':'done'})
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
    json_data = json.loads(request.body)   
    if json_data.get('idDr') == None:
        return JsonResponse({'message':'insert idDr'})    
    if json_data.get('NationalIDPationt') == None:
        return JsonResponse({'message':'insert NationalIDPationt'})    
    if json_data.get('drugllist') == None:
        return JsonResponse({'message':'insert drugllist'})    
    if json_data.get('comment') == None:
        return JsonResponse({'message':'insert comment'})    
    r = requests.post(USERS + "doExist", data=json.dumps({"p":json_data.get('NationalIDPationt'), "d":json_data.get('idDr')})) 
    a = r.json()
    if a.get('m') == False:
        return JsonResponse({"error":a.get('error')})    
    
    r = requests.post(PRESCRIPT + "dr/addPrescription", data=json.dumps(json_data)) 
    a = r.json()
    
    return JsonResponse(a)

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
    json_data = json.loads(request.body)   
    r = requests.post(USERS + "doExist", data=json.dumps({"p":json_data.get('id'), "d":1})) 
    a = r.json()
    if a.get('m') == False:
        return JsonResponse({"error":a.get('error')})    
    r = requests.post(PRESCRIPT + "p/listpres", data=json.dumps(json_data)) 
    a = r.json()
    return JsonResponse(a)
    
def admin_login(request):
    json_data = json.loads(request.body)   
    r = requests.post(USERS + "a/login", data=json.dumps(json_data)) 
    a = r.json()
    return JsonResponse(a)


def admin_getProfile(request):
    json_data = json.loads(request.body)   
    r = requests.post(USERS + "a/getProfile", data=json.dumps(json_data)) 
    a = r.json()
    return JsonResponse(a)

# return {totalPres, totalPatient, totalDr}
def admin_getstatistics(request):
    r = requests.post(USERS + "a/stat", ) 
    a = r.json()
    r = requests.post(PRESCRIPT + "a/stat",) 
    b = r.json()
    a.update(b)
    return JsonResponse({'message':a})
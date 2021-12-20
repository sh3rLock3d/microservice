from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.



def index(request):
    return JsonResponse({'foo':'bar'})
    #return HttpResponse('res':"Hello, world. You're at the polls index.")


# {name, nationalCode, password} return {id}
def dr_signin(request):
    return JsonResponse({'message':'done'})

# {nationalCode, password} return {id}
def dr_login(request):
    return JsonResponse({'message':'done'})

# {id} return {name, nationalCode}
def dr_get_profile(request):
    return JsonResponse({'message':'done'})

# {idDr, NationalIDPationt, [...drugllist], comment} return {done}
def dr_addPrescription(request):
    # check if pationt exists
    return JsonResponse({'message':'done'})

################

# {name, nationalCode, password} return {id}
def p_signin(request):
    return JsonResponse({'message':'done'})

# {nationalCode, password} return {id}
def p_login(request):
    return JsonResponse({'message':'done'})

# {id} return {name, nationalCode}
def p_get_profile(request):
    return JsonResponse({'message':'done'})

# {id} return {[...,list of prescript], [..., list of drs]}
def p_listpres(request):
    return JsonResponse({'message':'done'})

def admin_login(request):
    return JsonResponse({'message':'done'})


def admin_getProfile(request):
    return JsonResponse({'message':'done'})


def admin_getstatistics(request):
    return JsonResponse({'message':'done'})
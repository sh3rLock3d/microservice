from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index(request):
    return JsonResponse({'foo':'bar'})
    #return HttpResponse('res':"Hello, world. You're at the polls index.")

def dr_signin(request):    
    return JsonResponse({'foo':'bar'})
    #return HttpResponse('res':"Hello, world. You're at the polls index.")


def dr_signin(request):    
    return JsonResponse({'foo':'bar'})

def dr_login(request):    
    return JsonResponse({'foo':'bar'})

def dr_get_profile(request):    
    return JsonResponse({'foo':'bar'})

def p_signin(request):    
    return JsonResponse({'foo':'bar'})

def p_login(request):    
    return JsonResponse({'foo':'bar'})

def p_get_profile(request):    
    return JsonResponse({'foo':'bar'})

def admin_login(request):    
    return JsonResponse({'foo':'bar'})


def admin_getProfile(request):    
    return JsonResponse({'foo':'bar'})
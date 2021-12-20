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
    return JsonResponse({'foo':'bar'})

@csrf_exempt 
def p_listpres(request):
    return JsonResponse({'foo':'bar'})

@csrf_exempt 
def admin_getstatistics(request):
    return JsonResponse({'foo':'bar'})
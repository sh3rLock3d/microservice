from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.

def index(request):
    return JsonResponse({'foo':'bar'})
    #return HttpResponse('res':"Hello, world. You're at the polls index.")



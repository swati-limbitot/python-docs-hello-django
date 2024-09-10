from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("********** -( Hi Microland Team, we are learning App-Architecture ~!! )-**************** ")
 

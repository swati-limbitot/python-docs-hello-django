from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("********** -( Hi Team good Afternoon, Today we are happy ~!! ) **************** ")
 

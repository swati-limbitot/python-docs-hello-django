from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("********** -( Hi Team good Evening, Today we are happy & its beatifull day ~!! ) **************** ")
 

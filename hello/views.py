from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("********** -( Hi HPE Team good evening, My Name is '*****', We are learning AZURE Cloud Computing[AZ900] ) **************** ")

from django.shortcuts import render
from django.http import HttpResponse

def project(request, pk):
    return HttpResponse('Hello' + ' ' + str(pk))




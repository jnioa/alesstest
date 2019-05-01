from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'alesstest/jump.html')

from time import sleep

def timelimit(request):
    for i in range(10,-1,-1):
        sleep(1)
    return HttpResponse('end')
# Create your views here.

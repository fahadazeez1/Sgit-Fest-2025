from django.shortcuts import render,redirect
from django.contrib import admin
# Create your views here.
def starthome(request):
    return render(request,'index.html')

def toreg(request):
    return render(request,'regis.html')

def toindex(request):
    return render(request,'index.html')


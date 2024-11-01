from django.shortcuts import render,redirect
from django.contrib import admin
from myweb import models
from myweb.models import Registration2
# Create your views here.
def starthome(request):
    return render(request,'index.html')

def toreg(request):
    if request.method=="POST":
        name=request.POST.get('username')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        game=request.POST.get('games')
        detail=Registration2(name=name,email=email,game=game,dob=dob)
        detail.save()
        return redirect('home')
    return render(request,'regis.html')

def toindex(request):
    return render(request,'index.html')

def toex(request):
    return render(request,'index.html')

def obj(request):
    if request.method=="POST":
        name=request.POST.get('username')
        email=request.POST.get('email')
        dob=request.POST.get('dob')
        game=request.POST.get('games')
        detail=Registration2(name=name,email=email,game=game,dob=dob)
        detail.save()
        return redirect('home')
    return render(request, 'regis.html')    
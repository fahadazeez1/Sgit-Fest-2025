from django.shortcuts import render,redirect,HttpResponse
from django.contrib import admin
from myweb import models
from myweb.models import Registration2
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login as auth_login 
from django.contrib.auth import authenticate
# Create your views here.
from django.contrib import messages
def starthome(request):
    return render(request,'index.html')

# def toreg(request):
#     if request.method=="POST":
#         name=request.POST.get('username')
#         email=request.POST.get('email')
#         dob=request.POST.get('dob')
#         game=request.POST.get('games')
#         detail=Registration2(name=name,email=email,game=game,dob=dob)
#         detail.save()
#         return redirect('home')
#     return render(request,'regis.html')
def toreg(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        game = request.POST.get('games')
        try:
            registration = Registration2(name=name, email=email, dob=dob, game=game)
            registration.saves()
            return render(request, 'thnks.html')
        except ValidationError as e:
            return render(request, 'regis.html', {'error_message': str(e)})
        except IntegrityError:
            return render(request, 'regis.html', {'error_message': "This email is already registered."})
    
    return render(request, 'regis.html')
        
    #     try:
    #         # Attempt to create a new Registration2 record
    #         registration = Registration2(name=name, email=email, dob=dob, game=game)
    #         registration.saves()
    #         return render(request,'thnks.html')
    #     except ValidationError as e:
    #         # Display error message for duplicate email
    #         return render(request, 'regis.html', {'error_message': e.message})
    
    # return render(request, 'regis.html')





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


def tologadmin(request):

    return render(request,'adminlogin.html')
def tonav(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Logs the user in and creates a session
            return redirect('/admin/')  # Redirect to the admin/main page
        else:
            # messages.error(request, "Invalid username or password.")  # Error for invalid credentials
            return render(request, 'asa.html')
    return render(request,'asa.html')



def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Logs the user in and creates a session
            return redirect('/admin/')  # Redirect to the admin/main page
        else:
            messages.error(request, "Invalid username or password.")  # Error for invalid credentials
            return render(request, 'login.html')  # Stay on login page with error message

    return render(request, "login.html")
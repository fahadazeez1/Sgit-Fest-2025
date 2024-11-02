from django.shortcuts import render,redirect,HttpResponse
from django.contrib import admin
from myweb import models
from myweb.models import Registration2 , basket
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
            return render(request, 'newthx.html')
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
            messages.add_message(request, messages.ERROR, "Invalid username or password.")

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




def tobasket(request):
    if request.method=="POST":
        teamname=request.POST.get('teamname')
        captain=request.POST.get('captain')
        mob=request.POST.get('mob')
        # player1=request.POST.get('player1')
        player2=request.POST.get('username2')
        player3=request.POST.get('username3')
        player4=request.POST.get('username4')
        player5=request.POST.get('username5')
        player6=request.POST.get('username6')
        player7=request.POST.get('username7')
        player8=request.POST.get('username8')
        player9=request.POST.get('username9')
        player10=request.POST.get('username10')

        try:
            reg = basket(teamname=teamname, captain=captain, mob=mob, player2=player2, 
                         player3=player3, player4=player4, player5=player5, player6=player6,
                         player7=player7, player8=player8, player9=player9, player10=player10)
            reg.save()
            return render(request, 'baskeetball.html', {'success': "Team registered successfully!"})
        except (IntegrityError, ValidationError) as e:
            return render(request, 'baskeetball.html', {'error_message': str(e)})

    return render(request, 'baskeetball.html')

def basthk(request):
    if request.method=="POST":
        teamname=request.POST.get('teamname')
        captain=request.POST.get('captain')
        mob=request.POST.get('mob')
        # player1=request.POST.get('player1')
        player2=request.POST.get('username2')
        player3=request.POST.get('username3')
        player4=request.POST.get('username4')
        player5=request.POST.get('username5')
        player6=request.POST.get('username6')
        player7=request.POST.get('username7')
        player8=request.POST.get('username8')
        player9=request.POST.get('username9')
        player10=request.POST.get('username10')
        context={
            'name':teamname
        }
        try:
            reg = basket(teamname=teamname, captain=captain, mob=mob, player2=player2, 
                         player3=player3, player4=player4, player5=player5, player6=player6,
                         player7=player7, player8=player8, player9=player9, player10=player10)
            reg.save()
            return render(request, 'newthx.html', context=context)
        except (IntegrityError, ValidationError) as e:
            return render(request, 'baskeetball.html', {'error_message': str(e)})
    return render(request,'newthx.html')


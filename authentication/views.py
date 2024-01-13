from gzip import FNAME
from imaplib import _Authenticator
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout

import authentication





# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):    

    if request.method == "POST":
        usernames = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email= request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('cpassword') 
        
        myuser = User.objects.create_user(usernames,email,pass1)
        myuser.first_name =fname
        myuser.last_name =lname
        myuser.save()

        messages.success(request, "Your account has been created")
        # print("Im inside post")

        return redirect(reverse('signin'))

    return render(request, "authentication/signup.html")


def signin(request):
    
    if request.method == "POST":
            usernames = request.POST.get('username')
            pass1 = request.POST.get('password')

            user = authenticate(username = usernames,password=pass1)

            if user is not None:
                 login(request, user)
                 return redirect(reverse('home'), {'fname': FNAME})
                #  return redirect(reverse('home'))



            else:
                 messages.error(request, "Bad credentials")
                 return redirect(reverse('home'))




    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect('home')


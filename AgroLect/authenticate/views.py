from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        print(pass1,username)
        user = authenticate(username=username, password=pass1)

        print(user)
        if user is not None:
            login(request, user)
            print(messages.success(request, "Logged in Successfully"))
            return redirect('home')
        else:
            messages.error(request, "Bad Credentials!! Try Again")
            return redirect('login')
    return render(request,'login.html')

def signup(request):
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try a unique username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20 :
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')

        if len(pass1)<8:
            messages.error(request,"Password Must contain a minimum of 8 characters")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, pass1)
        # myuser.is_active = False
        u = User.objects.get(username=username)
        u.set_password(pass1)
        u.save()
        print(username,pass1)
        messages.success(request, "Your Account has been created succesfully!!")
        return redirect('login')
    return render(request,'signup.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('login')
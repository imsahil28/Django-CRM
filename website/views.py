from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
# Create your views here.

def home(request):
    
    if request.method =='POST':
        username= request.POST.get("username")
        password= request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"you have been logged in!")
            return redirect('home')
        else:
            messages.success(request,"there was error try again")
            return redirect('home')
    else:
        return render(request,'home.html',{})


from django.contrib import messages

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})

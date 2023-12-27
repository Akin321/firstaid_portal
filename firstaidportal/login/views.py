from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from login.models import CustomUser


# Create your views here.
def login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('Password')
        user=auth.authenticate(username=username,password=password)
        if user is not None and not user.is_administrator:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credntials')
            return redirect('login:login')

    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('psw')
        cpassword=request.POST.get('psw-repeat')
        if password == cpassword:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('login:register')
            else:
                user=CustomUser.objects.create_user(username=username,password=password)
                user.save()
                print('user registered')
                return redirect("login:login")
        else:
            messages.info(request,'password not matching')
            return redirect("login:register")

    else:
        return render(request,"registration.html")

def logout(request):
    auth.logout(request)
    return redirect(reverse('login:login'))

def admin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('Password')
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_administrator:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credntials')
            return redirect('login:admin_page')

    return render(request,'login.html',{'user_type':'admin'})
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import *

def register(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        if username and password:
            User.objects.create_user(
                username = username,
                password = password
            )
        return redirect('loginn')
    return render(request,'registration.html')


def loginn(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(
        request,
        username = request.data.get('username'),
        password = request.data.get('password')
        )
        if user is not None:
            login(request,user)
        return redirect('home')
    return render(request, 'login.html')
    
    
    
    
@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


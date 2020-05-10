from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('Blog:home')
            else:
                return redirect('Accounts:signup')
        else:
            messages.success(request, 'Username already exists, Please try another username!')
            return redirect('Accounts:signup')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def Login(request):
    if request.user.is_authenticated:
        return redirect('Accounts:accManage')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('Blog:home')
            else:
                return redirect('Accounts:login')
        else:
            return redirect('Accounts:login')
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':AuthenticationForm()})

def Logout(request):
    logout(request)
    return redirect('Blog:home')


def accManage(request):
    return render(request,'accManage.html')

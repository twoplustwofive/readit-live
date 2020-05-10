from django.shortcuts import render
from django.http import HttpResponse

def Hompage(request):
    return render(request,'../templates/homepage.html')

from django.shortcuts import render, redirect
from .models import Article
from .import forms
# Create your views here.
from django.contrib.auth import authenticate
def home(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'index.html',{'articles':articles})

def article_details(request,slug,id):
    article = Article.objects.get(pk=id)
    return render(request,'post.html',{'article':article})

def about(request):
    return render(request,'about.html')


def write(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.CreateArticle(request.POST,request.FILES)
            if form.is_valid:
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('Blog:home')
        else:
            form = forms.CreateArticle()
        return render(request,'CreateArticle.html',{'form':form})
    else:
        return redirect('Accounts:accManage')

def contact(request):
    if request.method == 'POST':
        form = forms.CreateContact(request.POST)
        if form.is_valid:
            form.save()
            return redirect('Blog:contact')
        else:
            return redirect('Blog:contact')
    else:
        form = forms.CreateContact()
    return render(request,'contact.html',{'form':form})

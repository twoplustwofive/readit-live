from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',default='media/images/default.jpg')
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]+'...'

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name

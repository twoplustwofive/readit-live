from django import forms
from .import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','slug','body','image']

class CreateContact(forms.ModelForm):
    class Meta:
        model = models.contact
        fields = ['name','email','phone','message']

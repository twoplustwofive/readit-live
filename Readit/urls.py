from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('accounts/',include('accounts.urls')),
]

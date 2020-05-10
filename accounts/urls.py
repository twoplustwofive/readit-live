from django.conf.urls import url, include
from .import views
from django.urls import path
app_name = 'Accounts'
urlpatterns =[
    path('signup',views.Signup,name='signup'),
    path('login',views.Login,name='login'),
    path('',views.accManage,name='accManage'),
    path('logout',views.Logout,name='logout'),
]

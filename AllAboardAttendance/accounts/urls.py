from django.contrib import admin
from django.urls import path
from . import views

'''
http://127.0.0.1:8000/accounts/signup leads to signup page. Same for login, logout. 
/accounts is our temporary home page. I think after Wesley adds some of our home pages, 
we may not use below home anymore. 
login, logout, signup can be directed from our own home page. 

Home page(login, signup) ==> Course page(has list of Sessions) ==> Session page. 
'''

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='home'),
]
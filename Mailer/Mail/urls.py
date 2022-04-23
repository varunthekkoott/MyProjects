from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('login/index/<int:id>/', views.pick, name='pick'),
    path('signup/', views.signup, name='signup'),
    path('check/', views.signcheck, name='signup'),
    path('login/index/<int:id>/inbox/', views.inbox, name='inbox'),
    path('login/index/<int:id>/inbox/<int:num>', views.mail, name='mail'),
    path('login/index/<int:id>/sendmail/', views.sendmail, name='sendmail'),
    path('login/index/<int:id>/sendmail/check/', views.checksendmail, name='checksendmail')
]

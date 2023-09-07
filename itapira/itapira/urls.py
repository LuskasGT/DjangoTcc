from django.contrib import admin
from django.urls import path
from tcc import views

urlpatterns = [
    #rota, view rsponsavel, nome de referência
    path('',views.home, name="home"),
]

from django.urls import path
from tcc import views

urlpatterns = [
    path('',views.index,name="index"),
]

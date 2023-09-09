from django.urls import path
from tcc import views

urlpatterns = [
    path ('',views.index,name="index"),
    path ('fale-conosco', views.faleConosco, name="faleConosco"),
    path ('adote', views.adote, name="adote"),
]

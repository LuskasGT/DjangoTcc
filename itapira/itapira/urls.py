from django.urls import path
from tcc import views

urlpatterns = [
    path('', views.index, name="index"),
    path('fale-conosco/', views.faleConosco, name='fale-conosco'),
    path('adote', views.adote, name='adote'),
    path('forms-bolt/', views.formsBolt, name="formsBolt"),
    path('forms-lola/', views.formsLola, name="formsLola"),
    path('forms-mia/', views.formsMia, name="formsMia"),
    path('forms-rex/', views.formsRex, name="formsRex"),
    path('forms-safira/', views.formsSafira, name="formsSafira"),
    path('forms-thor/', views.formsThor, name="formsThor"),
    path('porque-adotar/', views.porqueAdotar, name="porqueAdotar"),
]

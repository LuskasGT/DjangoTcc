from django.shortcuts import render

def index(request):
    return render(request,'tcc/index.html')

def faleConosco(request):
    return render(request,'tcc/fale-conosco.html')

def adote(request):
    return render(request,'tcc/adocao.html')
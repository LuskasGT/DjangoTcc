from django.shortcuts import render

def index(request):
    return render(request, 'tcc/index.html')

def faleConosco(request):
    return render(request, 'tcc/fale-conosco.html')

def adote(request):
    return render(request, 'tcc/adocao.html')

def formsBolt(request):
    return render(request, 'tcc/formsBolt.html')

def formsLola(request):
    return render(request, 'tcc/formsLola.html')

def formsMia(request):
    return render(request, 'tcc/formsMia.html')

def formsRex(request):
    return render(request, 'tcc/formsRex.html')

def formsSafira(request):
    return render(request, 'tcc/formsSafira.html')

def formsThor(request):
    return render(request, 'tcc/formsThor.html')

def porqueAdotar(request):
    return render(request, 'tcc/porqueAdotar.html')

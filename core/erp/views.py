from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from config import settings
from core.erp.forms import FormularioContacto


def myfirstview(request):
    return render(request,'home.html')

def servicios(request):
    return render(request,'servicios.html')


def nosotros(request):
    return render(request,'nosotros.html')


def casos(request):
    return render(request,'casos.html')


def tableta(request):
    return render(request,'tableta.html')

def contacto(request):
    if request.method == "POST":
        miFormu = FormularioContacto(request.POST)
        if miFormu.is_valid():
            infForm = miFormu.cleaned_data
            send_mail(infForm['asunto'],infForm['mensaje'],infForm.get('email',''),['hectorhugo359@gmail.com'],)
            return render(request,"home.html")
    else:
        miFormu = FormularioContacto()

    return render(request, "contacto.html", {"form":miFormu})
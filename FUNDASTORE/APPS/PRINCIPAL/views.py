from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
from .forms  import *

# Create your views here.
def inicio(request):
    banners = Banner.objects.all()
    contexto = {"banners":banners}
    return render(request, 'inicio.html',context=contexto)

def nostros(request):
    return render(request, 'nosotros.html')

def ver_contactenos(request):
    formulario = FormularioContactenos()
    if request.method == "POST":
        formulario = FormularioContactenos(request.POST)
        asunto = 'CONSULTA DE - ' + str(formulario["nombre"].value())
        mensaje = 'INFORMACION DE CONTACTO\nNOMBRE: [NOM]\nEMAIL: [EMAIL]\nTELEFONO: [TEL]\n\nMESNAJE\n[MSJ]'
        mensaje =mensaje.replace("[NOM]",formulario["nombre"].value())
        mensaje =mensaje.replace("[EMAIL]",formulario["email"].value())
        mensaje =mensaje.replace("[TEL]",formulario["telefono"].value())
        mensaje =mensaje.replace("[MSJ]",formulario["mensaje"].value())
        destinatarios = ["rmclaudio22@ymail.com"]
        send_mail(asunto,mensaje,None,destinatarios,fail_silently=False)
        
        asunto = 'SU CONSULTA HA SIDO RECIBIDA'
        mensaje = 'HEMOS  RECIBIDO SU CONSULTA, TENDRA UNA RESPUESTA EN LOS SIGUIENTES 3 DIAS HABILES'
        destinatarios = [str(formulario["email"].value())]
        send_mail(asunto,mensaje,None,destinatarios,fail_silently=False)
    else:
        formulario = FormularioContactenos()
    contexto = {"formulario":formulario}
    return render(request,'PRINCIPAL/contactenos.html',contexto)


def recetas(request):
    blogs = Blog.objects.filter(blg_tipo='R')
    contexto = {"recetas":blogs}
    return render(request, 'PRINCIPAL/BLOG/RECETAS/recetas.html', context=contexto)
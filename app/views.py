from django.shortcuts import render
from .cifrado import Cifrado
from .models import cifrado
from django.shortcuts import redirect
from django.http import JsonResponse
from django.core import serializers
from django.db import connection
from .forms import PostForm
# Create your views here.
def inicio(request):
    cifrarT = cifrado.objects.all()
    lastValue = cifrado.objects.count()
    modo = 'encriptar'
    clave = 3
    mensaje = 'hola mundo'
    cifrar = Cifrado.obtenerMensajeTraducido(modo,mensaje,clave)
 
    if request.method == "POST":

        apodo = request.POST['apodo']
        modo = 'encriptar'
        clave = int(request.POST['clave'])
        mensaje = request.POST['mensaje']
        cifrar = Cifrado.obtenerMensajeTraducido(modo,mensaje,clave)
        with connection.cursor() as cursor: 
            cursor.execute("INSERT INTO app_cifrado(nickname,message,key) VALUES ('{apodo}', '{mensaje}', '{clave}')".format( apodo=apodo, mensaje=cifrar, clave=clave))
            cursor.fetchone()
            return redirect('/')

    try:
        variable = request.POST['buscando']
        
        with connection.cursor() as cursor: 
            cursor.execute("SELECT message FROM app_cifrado WHERE id = "+ variable )
            consulta = cursor.fetchone()

    except:
        consulta = ["xd"]
     
    #cifrar = Cifrado.obtenerMensajeTraducido(modo,mensaje,clave)

    contexto = {'cifrarT': cifrarT,'lastValue':lastValue, 'consulta':consulta[0] }
    return render(request, 'index.html', contexto)
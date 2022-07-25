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
    cod_cifrado=""
    consulta = ""
    llave =0
    cifrarT = cifrado.objects.all()
    lastValue = cifrado.objects.count()
    modo = 'encriptar'
    clave = 3
    mensaje = 'hola mundo'
    cifrar = Cifrado.obtenerMensajeTraducido(modo,mensaje,clave)
    try:
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
    except:
        try:
            variable = request.POST['buscando']
            clave = int(request.POST['texto'])
            with connection.cursor() as cursor: 
                cursor.execute("SELECT message,key, id FROM app_cifrado WHERE id = "+ variable )
                consultax = cursor.fetchone()

                if consultax[1] == str(clave):
                    consulta = Cifrado.obtenerMensajeTraducido('desencriptar',consultax[0],clave)
                    llave = 1
                    cod_cifrado = consultax[2] 
                else:
                    consulta = "La clave ha sido incorrecta" 

        except:
            consulta = ""
    

        #cifrar = Cifrado.obtenerMensajeTraducido(modo,mensaje,clave)

    contexto = {'cifrarT': cifrarT,'lastValue':lastValue, 'consulta':consulta ,  'llave':llave, 'cod_cifrado' :cod_cifrado}
    return render(request, 'index.html', contexto)

def delete(request, pk):
    try:
        record = cifrado.objects.get(id = pk)
        record.delete()
        return redirect('/')
    except:
        print("Record doesn't exists")
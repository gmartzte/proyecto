from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import Context, Template
from apps.models import *
from apps.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

def inicio(request):
	return render(request, "base.html")

def principal(request):
    return render(request, "inicio.html") 

def vista(request):
    return render(request, "vista.html")  

def upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST.get('titulo', '')
            archivo = request.FILES.get('archivo', '')
            autor = Usuario.objects.get(id = request.session['id'])
            video = Video(titulo = titulo, archivo = archivo, usuario = autor)
            video.save()
            try:
                return render(request, "vista.html")
            except:
                error = 'Error. Intente más tarde'
                return render_to_response('subir.html',{'error':error})

        else:
            form = VideoForm(request.POST, request.FILES)
            error = "Algunos campos son inválidos"
            return render(request, "subir.html", {
                'form': form,
                'error': error
            })
    else:
        form = VideoForm()
        return render(request, "subir.html", {
                'form': form,
            })

def datosVideo(request):
    videos = Video.objects.all()
    return render_to_response('vista.html', {'video': videos})

def ultimo(request):
    video = Video.objects.latest('id')
    return render_to_response('vista.html', {'video': videos})

@csrf_exempt
def accionIniciar(request):
    if request.method == 'POST':
        user = request.POST.get('username','') #Podría hacerse con ['usuario'] pero si no encuentra la llave generaría un error
        password = request.POST.get('contrasena','')
        print(user,password)
        if not user or not password:
            error = 'Faltan campos por llenar'
            return render_to_response('inicio.html',{'error':error}) 
        try:
            usuario = Usuario.objects.get(username = user, contrasena = password) 
            request.session['logueado'] = True
            request.session['username'] = user
            request.session['id'] = usuario.id
            usuario = Usuario.objects.get(username=user)
            print("INICIO",request.session['id'])
            return redirect("/lista/")
        except: 
            error = 'Usuario o contraseña inválidos'
            return render_to_response('inicio.html',{'error':error})

@csrf_exempt
def accionRegistrar(request):
    nombre = request.POST.get('nombre', '')
    user = request.POST.get('username', '')
    correo = request.POST.get('correo', '')
    password = request.POST.get('contrasena','')
    if not nombre or not user or not correo or not password:
        error = 'Faltan campos por llenar'
        return render_to_response('inicio.html', {'error':error})
    try:
        usuario = Usuario(nombre = nombre, username = user, 
            correo = correo, password = contrasena)
        usuario.save()
        pritnt("Usuario registrado")
        return redirect("/principal/")
    except:
        error = {"error": "El usuario ya está registrado"}
        return render_to_response('inicio.html', error)

def salir(request):
    request.session['logueado'] = False
    return redirect("/principal/")

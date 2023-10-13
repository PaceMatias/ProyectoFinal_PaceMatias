from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from AppLogin.forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from AppLogin.models import Avatar

# Create your views here.

def inicio_sesion(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 
            
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contra)

            if user:
                login(request, user)

                return render(request, "AppBalti/inicio.html", {"mensaje":f"Hola, {usuario}!"})
                     
        else:
            form = AuthenticationForm()    
            return render(request, "AppLogin/login.html", {"mensaje":"Usuario o contraseña incorrectos","form": form})

    form = AuthenticationForm()

    return render(request, "AppLogin/login.html", {"form": form})


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
          usuario = form.cleaned_data['username']
          form.save()
          return render(request, "AppBalti/inicio.html", {"mensaje":f"Se creo el usuario: {usuario}"})

    else:
        form = RegistroUsuario()     

    return render(request,"AppLogin/registro.html" ,  {"form":form})

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = EditarUsuario(request.POST)
        if form.is_valid():
          info = form.cleaned_data

          usuario.email = info['email']
          usuario.set_password(info['password1']) 
          usuario.first_name = info['first_name']

          usuario.save()
          return render(request, "AppBalti/inicio.html", {"mensaje":f"Se modifico el usuario: {usuario}"})

    else:
        form = EditarUsuario(initial={'email': usuario.email,'first_name': usuario.first_name})
    
    return render(request, "AppLogin/editar_usuario.html", {"form":form, "usuario": usuario})

@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        form = Avatar_Form(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username = request.user)
            imagen = form.cleaned_data['imagen']
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            # Redirigir a alguna página de éxito o realizar alguna otra acción
            return render(request, "AppBalti/inicio.html")  # Asegúrate de reemplazar 'nombre_de_la_vista_de_exito' con la vista que desees

    else:
        form = Avatar_Form()
    
    return render(request, "AppLogin/agregar_avatar.html", {"form": form})



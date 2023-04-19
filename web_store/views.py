from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import RegisterForm
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html', {
        # Context -> podemos pasar valores de nuestra vista a un template
        'message':'Listado de Productos',
        'title': 'Productos',
        'products': [
            {'title': 'Playera', 'price': 5, 'stock': True}, # Producto
            {'title': 'Camisa', 'price': 7, 'stock': True},
            {'title': 'Mochila', 'price': 20, 'stock': False},
            {'title': 'Gorra J&G', 'price': 10, 'stock': True}
        ]
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') # diccionario
        password = request.POST.get('password') # retorna el valor de la llave o por el contrario None
        
        user = authenticate(username=username, password=password) # Sino encuentra coincidencia retorna None
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
        
    return render(request, 'users/login.html', {
        
    })


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect ('login')


def register(request):
    form = RegisterForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        # Obtain information from form
        # username = form.cleaned_data.get('username') # Dictionary
        # email = form.cleaned_data.get('email')
        # password = form.cleaned_data.get('password')
        
        # Create a user without administrator permissions
        # user = User.objects.create_user(username, email, password)
        user = form.save()
        if user:
            login(request, user) # Creando la sesión
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
        
    return render(request, 'users/register.html', {
        'form': form
    })
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login

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
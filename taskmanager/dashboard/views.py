from django.shortcuts import render


# Create your views here.

def login(request):

    context = {"title": "Login Task-Manager",
               "presentation": "Olá, bem vindo ao Task-Manager!",
               "start": "TESTE",
               }

    return render(request, "login.html", context)

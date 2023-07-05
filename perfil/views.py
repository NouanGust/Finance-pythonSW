from django.shortcuts import render
from django.http import HttpResponse

# Criando a função da página, precisa receber o request e retornar uma resposta
def home(request):
    return render(request, 'home.html')
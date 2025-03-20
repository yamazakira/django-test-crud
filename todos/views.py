from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Meio-termo entre back e front; processa as requisições das páginas;


def home(request):
    return render(request, "todos/home.html")

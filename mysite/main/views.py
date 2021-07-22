from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, ToDoList

# Create your views here.
def index(response, name):
    ls = ToDoList.objects.get(name=name)
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    ls = ToDoList.objects.all()
    return render(response, "main/home.html", {"list": ls})
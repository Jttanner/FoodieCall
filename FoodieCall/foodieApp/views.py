from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def login(request):
    return render(request, 'home/login.html')

def register(request):
    return render(request, 'home/register.html')

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
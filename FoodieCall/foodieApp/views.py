from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models.Users import Users
import json
from datetime import datetime

from .forms.LoginForm import LoginForm
from .forms.RegisterForm import RegisterForm

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        try:  #success
            loginUser = Users.object.get(email=form.email, password=form.password)
            return render(request, 'home/dashboard.html')
        except:
            return render(request, 'home/home.html')
    else:
        return render(request, 'home/home.html')  #only accept posts

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        try:
            checkExistingEmail = Users.object.get(email=form.email)
            checkExistingDisplayName = Users.object.get(display_name=form.display_name)
            return render(request, 'home/register.html')
        except:
            newUser = Users(display_name=form.display_name, email=form.email, password=form.password, first_name=form.first_name, last_name=form.last_name, date_registered=datetime.now())
    else:
        return render(request, 'home/register.html')

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
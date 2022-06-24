from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Team


# Create your views here.
def home(request):
    obj = Team.objects.all()
    return render(request, "index.html", {'output': obj})



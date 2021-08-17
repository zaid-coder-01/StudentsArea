from django.shortcuts import render
import requests

# Create your views here.
from apps.models import Facts


def index(request):
    facts = Facts.objects.all()
    return render(request, "index.html", {"facts": facts})


def resume(request):
    return render(request, "resume.html")


def career(request):
    return render(request, "resumeTemplate.html")


def login(request):
    return render(request, "login.html")


def math(request):
    return render(request, "maths.html")

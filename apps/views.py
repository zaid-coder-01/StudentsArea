from django.shortcuts import render
import requests

# Create your views here.
from apps.models import Facts, Document


def index(request):
    facts = Facts.objects.all()
    return render(request, "index.html", {"facts": facts})


def resume(request):
    return render(request, "resume.html")


def cheatsheet(request):
    return render(request, "cheetsheet.html")


def login(request):
    return render(request, "login.html")


def math(request):
    return render(request, "maths.html")


def studentpage(request):
    return render(request, "studentPage.html")


def note(request):
    return render(request, "notes.html")


def document(request):
    if request.method == 'POST':
        name = request.POST["name"]
        doc = request.POST["doc"]
        sa=Document(name=name,document=doc)
        sa.save()

    doc = Document.objects.all()
    return render(request, "document.html", {"doc": doc})


def datavisu(request):
    return render(request, "datavisu.html")


def tempdesign(request):
    return render(request, "templatedesign.html")


def resumeTemplate(request):
    return render(request, "resumeTemplate.html")

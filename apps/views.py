import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import requests
import sympy as sp
import numpy as np

# Create your views here.
from sympy import sympify, parse_expr

from apps.models import Facts, Document


def index(request):
    facts = Facts.objects.all()
    facts = list(facts)
    np.random.shuffle(facts)

    return render(request, "index.html", {"facts": facts})


def resume(request):
    return render(request, "resume.html")


def book(request):
    return render(request, "book.html")


def books(request):
    return render(request, "bookread.html")


def linear(request):
    if request.method == 'POST':
        eq1 = request.POST['eq1']
        eq2 = request.POST['eq2']
        v1 = request.POST['var1']
        v2 = request.POST['var2']
        c1 = request.POST['c1']
        c2 = request.POST['c2']
        v3 = str(v1) + "," + str(v2)
        print(eq1)
        print(eq2)
        print(v3)
        x, y = sp.symbols(v3)
        eq1 = sympify(eq1, evaluate=False)
        eq2 = sympify(eq2, evaluate=False)
        print(eq1)
        print(eq2)
        eq1 = sp.Eq(eq1, int(c1))
        eq2 = sp.Eq(eq2, int(c2))
        v = sp.solve((eq1, eq2), (x, y))
        v = str(v)
        return JsonResponse(v, safe=False)
    return render(request, "linear.html")


def linears(request):
    if request.method == 'POST':
        eq1 = request.POST['eq1']
        eq2 = request.POST['eq2']
        eq3 = request.POST['eq3']
        v1 = request.POST['var1']
        v2 = request.POST['var2']
        v3 = request.POST['var3']
        c1 = request.POST['c1']
        c2 = request.POST['c2']
        c3 = request.POST['c3']
        v3 = str(v1) + "," + str(v2) + "," + str(v3)
        print(eq1)
        print(eq2)
        print(v3)
        x, y, z = sp.symbols(v3)
        eq1 = sympify(eq1, evaluate=False)
        eq2 = sympify(eq2, evaluate=False)
        eq3 = sympify(eq3, evaluate=False)
        print(eq1)
        print(eq2)
        eq1 = sp.Eq(eq1, int(c1))
        eq2 = sp.Eq(eq2, int(c2))
        eq3 = sp.Eq(eq3, int(c3))
        v = sp.solve((eq1, eq2, eq3), (x, y, z))
        v = str(v)
        return JsonResponse(v, safe=False)


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
        sa = Document(name=name, document=doc)
        sa.save()

    doc = Document.objects.all()
    return render(request, "document.html", {"doc": doc})


def datavisu(request):
    return render(request, "datavisu.html")


def tempdesign(request):
    return render(request, "templatedesign.html")


def resumeTemplate(request):
    return render(request, "resumeTemplate.html")


def matrix(request):
    return render(request, "matrix.html")


def matrixs(request):
    if request.method == 'POST':
        r = request.POST["row"]
        c = request.POST["col"]
        m1 = request.POST["matA"]
        m2 = request.POST["matB"]

        a = []
        b = []
        for i in m1.split(','):
            a.append(int(i))

        for i in m2.split(','):
            b.append(int(i))

        a = np.array(a)
        b = np.array(b)
        a = a.reshape(int(r), int(c))
        b = b.reshape(int(r), int(c))
        ans = np.add(a, b)
        context = {
            "matA": a,
            "matB": b,
            "ans": ans
        }

        data = json.dumps(context, indent=4, sort_keys=True, default=str)
        return HttpResponse(data, content_type='application/json')


def science(request):
    return render(request, "science/science.html")


def humrespi(request):
    return render(request, "science/humrespi.html")

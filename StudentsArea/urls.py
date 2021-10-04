"""StudentsArea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .import settings
from apps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('resume/',views.resume),
    path('cheatsheet/',views.cheatsheet,name='save'),
    path('login/', views.login),
    path('maths/', views.math),
    path('studentPage/', views.studentpage),
    path('notes/', views.note),
    path('document/', views.document),
    path('datavisu/', views.datavisu),
    path('linear/', views.linear,name="linear"),
    path('linears/', views.linears, name="linears"),
    path('book/', views.book,name="book"),
    path('bookread/', views.books, name="bookread"),
    path('templatedesign/', views.tempdesign,name="tempdesign"),
    path('resumeTemplate/', views.resumeTemplate,name="resumeTemplate"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

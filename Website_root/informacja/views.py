from django.shortcuts import render, redirect
from crm.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import News
from django.http import HttpResponse
import smtplib
from email.mime.text import MIMEText
from django.contrib.auth.decorators import login_required
from crm.forms import ApplicationForm

def main_page(request):
    return render(request, 'index.html')

def nowosci(request):
    news = News.objects.all().order_by('-date')
    return render(request, 'wiadomosci.html', {'news': news})

def uslugi(request):
    return render(request, 'uslugi.html')

def promocje(request):
    return render(request, 'promocje.html')

def humor(request):
    return render(request, 'humor.html')

def rejestracja(request):
    return render(request, 'rejestracja.html')

def log_in(request):
    return render(request, 'login.html')

def polityka(request):
    return render(request, 'polityka-prywatnosci.html')

def error(request):
    return render(request, "error.html")
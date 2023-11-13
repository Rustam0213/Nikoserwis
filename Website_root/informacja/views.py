from .ps import password
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from .models import News
from django.http import HttpResponse
from crm.models import CrmSystem
import random
import smtplib
from email.mime.text import MIMEText
    
def main_page(request):
    news = News.objects.all().order_by('-date')
    return render(request, 'pl/index.html', {'news': news})

def o_nas(request):
    return render(request, 'pl/o_nas.html')

def uslugi(request):
    return render(request, 'pl/uslugi.html')

def promocje(request):
    return render(request, 'pl/promocje.html')

def humor(request):
    return render(request, 'pl/humor.html')

def rejestracja(request):
    return render(request, 'pl/rejestracja.html')

def log_in(request):
    return render(request, 'pl/login.html')


def kod(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        verify_code = str(random.randint(1000, 9999))

        send_email(email, verify_code)

        request.session['verify_code'] = verify_code  # Сохраняем код в сессии

        return render(request, 'pl/kod.html', {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'phone': phone,
            'password': password,
        })
    else:
        return render(request, 'pl/error.html')


def send_email(receiver_email, message):
    sender = "nikoserwisbot@gmail.com"
    password1 = password
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    msg = MIMEText(message)
    msg['Subject'] = "Twój kod werifikacyjny"
    server.login(sender, password1)
    server.sendmail(sender, receiver_email, msg.as_string())
    server.quit()


def wiadomosc(request):
    if request.method == "POST":
        numbers = request.POST['verify_code']
        verify_code = request.session.get('verify_code')
        if numbers == verify_code:
            return render(request, 'pl/wiadomosc.html')
        else:
            return render(request, 'pl/error.html')
    else:
        return render(request, 'pl/error.html')    

def resetpw(request):
    return render(request, 'pl/resetpw.html')

def newpw(request):
    return render(request, 'pl/newpw.html')

def kod2(request):
    return render(request, 'pl/kod2.html')

def writeemail(request):
    return render(request, 'pl/writeemail.html')

def polityka(request):
    return render(request, 'pl/polityka-prywatnosci.html')

def error(request):
    return render(request, "pl/error.html")
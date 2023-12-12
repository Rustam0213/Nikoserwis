from .ps import password
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import News
from django.http import HttpResponse
from crm.models import CrmSystem
import random
import smtplib
from email.mime.text import MIMEText
from crm.forms import CrmSystemForm, CustomCrmSystemForm
    
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
    if request.method == 'POST':
        form = CrmSystemForm(request.POST)

    return render(request, 'pl/rejestracja.html', {'form':form})

def log_in(request):
    login_form = CrmSystemForm()
    return render(request, 'pl/login.html', {'login_form':login_form})

def kod(request):
    if request.method == "POST":
        form_crm = CrmSystemForm(request.POST)
        if form_crm.is_valid():
            form_crm.save()
            verify_code = str(random.randint(10000, 99999))
            send_email(form_crm.cleaned_data['crm_email'], verify_code)
            request.session['verify_code'] = verify_code
            return render(request, 'pl/kod.html', {"form_crm": form_crm}) 
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

def login_alg(request):
    if request.method == "POST":
        login_form = CustomCrmSystemForm(request.POST)
        form = CrmSystemForm()
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, 
                                crm_email=cd['crm_email'], 
                                crm_password=cd['crm_password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    print(user.errors)
                    return render(request, 'pl/error.html')
                else:
                    return render(request, 'pl/error.html')  # change error.html to normal page
            else:
                return render(request, 'pl/rejestracja.html', {'form':form})
        else:
            print(login_form.errors)
            return render(request, 'pl/error.html')  # handle the case when form is not valid
    else:
        return render(request, 'pl/error.html')  # handle the case when request method is not POST


def writeemail(request):
    return render(request, 'pl/writeemail.html')

def polityka(request):
    return render(request, 'pl/polityka-prywatnosci.html')

def error(request):
    return render(request, "pl/error.html")
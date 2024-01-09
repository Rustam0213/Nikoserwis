from .ps import password
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
    news = News.objects.all().order_by('-date')
    return render(request, 'index.html', {'news': news})

def o_nas(request):
    return render(request, 'onas.html')

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

def kod(request):
    return render(request, 'kod.html')


'''def send_email(receiver_email, message):
    sender = "nikoserwisbot@gmail.com"
    password1 = password
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    msg = MIMEText(message)
    msg['Subject'] = "Twój kod werifikacyjny"
    server.login(sender, password1)
    server.sendmail(sender, receiver_email, msg.as_string())
    server.quit()'''


@login_required
def wiadomosc(request):
    user = request.user
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Создаем объект Applications с указанием пользователя в поле from_who
            application = form.save(commit=False)
            application.from_who = user
            application.save()
            return redirect('main_page')
        else:
            print(form.errors)
    else:
        form = ApplicationForm()
    
    return render(request, 'wiadomosc.html', {'user': user, 'form': form})


def resetpw(request):
    return render(request, 'resetpw.html')

def newpw(request):
    return render(request, 'newpw.html')

def writeemail(request):
    return render(request, 'writeemail.html')

def polityka(request):
    return render(request, 'polityka-prywatnosci.html')

def error(request):
    return render(request, "error.html")
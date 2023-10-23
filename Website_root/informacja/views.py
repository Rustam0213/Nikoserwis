from django.shortcuts import render
from .models import News
from crm.models import CrmSystem
from django.core.mail import send_mail

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

def wiadomosc(request):
    return render(request, 'pl/wiadomosc.html')

def log_in(request):
    return render(request, 'pl/login.html')

def kod(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    phone = request.POST['phone']
    email = request.POST['email']
    password = request.POST['password']
    
    element = CrmSystem(crm_name=firstname, crm_lastname=lastname, crm_number=phone, crm_email=email, crm_password=password)
    element.save()

    subject = 'Тема письма'
    message = 'Текст сообщения'
    from_email = 'nikoserwisbot@gmail.com'
    recipient_list = ['rdvelihanov1245@gmail.com']

    try:
        send_mail(subject, message, from_email, recipient_list)
        email_sent = True
    except Exception as e:
        email_sent = False
        error_message = str(e)

    return render(request, './kod.html', {
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'phone': phone,
        'password': password,
        'email_sent': email_sent,
        'error_message': error_message if not email_sent else None,
    })

def resetpw(request):
    return render(request, 'pl/resetpw.html')

def newpw(request):
    return render(request, 'pl/newpw.html')

def kod2(request):
    return render(request, 'pl/kod2.html')

def writeemail(request):
    return render(request, 'pl/writeemail.html')

def accept(request):
    return render(request, 'pl/accept.html')
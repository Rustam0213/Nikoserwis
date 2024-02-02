from django.shortcuts import render, redirect
from .forms import ApplicationForm, UserCreationForm, UserProfileForm, VerificationCodeForm
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from .ps import password
import smtplib
import random
from email.mime.text import MIMEText
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Applications, User
from django.http import Http404
from django.contrib import messages

@login_required
def user_profile(request):
    user = request.user

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('user_profile')
    else:
        profile_form = UserProfileForm(instance=user)

    return render(request, 'user_profile.html', {'profile_form': profile_form})

@login_required
def application_details(request, application_id):
    application = get_object_or_404(Applications, pk=application_id)
    if application.from_who != request.user:
        raise Http404("Error")

    return render(request, 'application_details.html', {'application': application})


@login_required
def profile(request):
    user_applications = request.user.get_user_applications().order_by('-date_created')

    return render(request, 'profile.html', {'user_applications': user_applications})


@login_required
def wiadomosc(request):
    user = request.user
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.from_who = user
            application.save()
            return redirect('main_page')
        else:
            print(form.errors)
    else:
        form = ApplicationForm()
    
    return render(request, 'wiadomosc.html', {'user': user, 'form': form})

def send_email(receiver_email, message):
    sender = "nikoserwisbot@gmail.com"
    password1 = password
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    message = str(message)
    
    msg = MIMEText(message)
    msg['Subject'] = "Twój kod werifikacyjny"
    server.login(sender, password1)
    server.sendmail(sender, receiver_email, msg.as_string())
    server.quit()

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': UserCreationForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            rand = random.randint(1000, 9999)
            request.session['verification_code'] = rand
            send_email(email, rand)
            user = form.save()
            return redirect('kod')

        context = {'form': form}
        return render(request, self.template_name, context)


def kod(request):
    if request.method == 'POST':
        form = VerificationCodeForm(request.POST)
        if form.is_valid():
            get_code = form.cleaned_data.get('verification_code')
            random_code = request.session.get('verification_code')
            email = request.session.get('email')
            password = request.session.get('password')

            if get_code == random_code:
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    del request.session['verification_code']
                    del request.session['email']
                    del request.session['password']
                    return redirect('profile')
            else:
                messages.error(request, 'Incorrect verification code. Please try again.')
        else:
            messages.error(request, 'Form error.')
    else:

        form = VerificationCodeForm()

    return render(request, 'registration/kod.html', {'form': form})


class CustomLoginView(View):
    template_name = 'registration/login.html'

    def get(self, request):
        context = {'form': AuthenticationForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
        context = {'form': form}
        return render(request, self.template_name, context)
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib.auth.forms import AuthenticationForm

class Register(View):
      
      template_name = 'registration/register.html'

      def get(self, request):
            context = {
                  'form': UserCreationForm(),
            }
            return render(request, self.template_name, context)

      def post(self, request):
            
            form = UserCreationForm(request.POST)

            if form.is_valid():
                  user = form.save()
                  login(request, user)
                  return redirect('wiadomosc')
            
            context = {
                  'form': form,
            }

            return render(request, self.template_name, context)

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
                return redirect('wiadomosc')
        context = {'form': form}
        return render(request, self.template_name, context)
    

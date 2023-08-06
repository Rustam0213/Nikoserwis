from django.shortcuts import render
from .models import News

def main_page(request):
    news = News.objects.all()
    return render(request, './wiadomosci.html',{'news':news})

def o_nas(request):
    return render(request, './o_nas.html')
def uslugi(request):
    return render(request, './uslugi.html')
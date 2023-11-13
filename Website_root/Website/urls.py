from django.contrib import admin
from django.urls import path
from informacja import views
from django.conf.urls.static import static
from django.conf import settings
import uuid


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name = 'main_page'),
    path('uslugi/', views.uslugi, name = 'uslugi'),
    path('informacja/', views.o_nas, name = 'o_nas'),
    path('promocje/', views.promocje, name = 'promocje'),
    path('humor/', views.humor, name = 'humor'),
    path('rejestracja/', views.rejestracja, name = 'rejestracja'),
    path('wiadomosc/', views.wiadomosc, name='wiadomosc'),
    path('login/', views.log_in, name = 'login'),
    path('kod/', views.kod, name = 'kod'),
    path('zmien-haslo/', views.resetpw, name = 'resetpw'),
    path('nowe-haslo/', views.newpw, name = 'newpw'),
    path('wpisz-email/', views.writeemail, name = 'writeemail'),
    path('wpisz-kod/', views.kod2, name = 'kod2'),
    path('polityka-prywatnosci/', views.polityka, name = 'polityka'),
    path('nipoprawny-kod/', views.error, name = 'error'),    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

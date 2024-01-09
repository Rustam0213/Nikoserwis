from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class User(AbstractUser):
      email = models.EmailField(_("email address"), unique = True)
      USERNAME_FIELD = "email"
      REQUIRED_FIELDS = ["username"]

      class Meta:
            verbose_name = 'Użytkownika'
            verbose_name_plural = 'Użytkownicy'

class Applications(models.Model):
      from_who = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Od kogo')
      date_created = models.DateTimeField(default=timezone.now, verbose_name='Data utworzenia')
      desired_appointment_date = models.DateField(null=True, blank=True, verbose_name='Data spotkania')
      vin_code = models.CharField(max_length=17, verbose_name='VIN')
      reg_num = models.CharField(max_length=20, verbose_name='Numer rejestracyjny')
      mark = models.CharField(max_length=100, verbose_name='Marka')
      model = models.CharField(max_length=100, verbose_name='Model')
      year = models.CharField(max_length=100, verbose_name='Rok')
      displacement = models.CharField(max_length=100, verbose_name='Pojemność silnika')
      hp = models.CharField(max_length=100, verbose_name='KM')
      details = models.TextField(verbose_name='Szczegóły problemu')
      

      def __str__(self):
            return "Nowy wniosek"

      class Meta:
            verbose_name = 'wniosek'
            verbose_name_plural = 'wnioski'
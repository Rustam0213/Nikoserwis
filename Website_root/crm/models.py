from django.db import models
from django.contrib.auth.hashers import make_password

class CrmSystem(models.Model):
    crm_name = models.CharField(max_length=50, verbose_name='Imię')  # Имя
    crm_lastname = models.CharField(max_length=50, verbose_name='Nazwisko')  # Фамилия
    crm_number = models.CharField(max_length=15, verbose_name='Numer')  # Номер контактного телефона
    crm_email = models.EmailField(verbose_name='Email')  # Электронная почта
    crm_password = models.CharField(max_length=128, verbose_name='Hasło')  # Пароль

    def save(self, *args, **kwargs):
        if not self.pk:
            self.crm_password = make_password(self.crm_password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.crm_email

    class Meta:
        verbose_name = 'Osobę'
        verbose_name_plural = 'Osoby'

# Generated by Django 5.0.1 on 2024-01-08 17:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin_code', models.CharField(max_length=17, verbose_name='VIN')),
                ('reg_num', models.CharField(max_length=20, verbose_name='Numer rejestracyjny')),
                ('mark', models.CharField(max_length=100, verbose_name='Marka')),
                ('model', models.CharField(max_length=100, verbose_name='Model')),
                ('year', models.CharField(max_length=100, verbose_name='Rok')),
                ('displacement', models.CharField(max_length=100, verbose_name='Pojemność silnika')),
                ('hp', models.CharField(max_length=100, verbose_name='KM')),
                ('details', models.TextField(verbose_name='Szczegóły problemu')),
                ('from_who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Od kogo')),
            ],
            options={
                'verbose_name': 'wniosek',
                'verbose_name_plural': 'wnioski',
            },
        ),
    ]

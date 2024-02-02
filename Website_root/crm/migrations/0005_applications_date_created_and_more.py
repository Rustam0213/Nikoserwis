# Generated by Django 5.0.1 on 2024-01-10 17:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_alter_applications_hp'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data utworzenia'),
        ),
        migrations.AddField(
            model_name='applications',
            name='desired_appointment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data spotkania'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='year',
            field=models.CharField(max_length=100, verbose_name='Rok'),
        ),
    ]

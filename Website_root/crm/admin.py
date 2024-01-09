from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Applications, User

class CustomUserAdmin(UserAdmin):
    list_display = ['first_name', 'last_name', 'email','phone', 'is_staff']  # Добавьте поля, которые вы хотите отображать
    search_fields = ['first_name', 'last_name', 'email','phone']

class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ['from_who', 'vin_code', 'reg_num', 'mark', 'model', 'year', 'displacement']
    search_fields = ['vin_code', 'reg_num', 'mark', 'model']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Applications, ApplicationsAdmin)

admin.site.site_header = 'Administracja Nikoserwis'

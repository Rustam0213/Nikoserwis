from django.contrib import admin
from .models import CrmSystem

class CrmSystemAdmin(admin.ModelAdmin):
    list_display = ('crm_name', 'crm_lastname', 'crm_number', 'crm_email')  # Отображаемые поля в списке
    exclude = ('crm_password',)  # Исключаем поле пароля из редактирования

admin.site.register(CrmSystem, CrmSystemAdmin)
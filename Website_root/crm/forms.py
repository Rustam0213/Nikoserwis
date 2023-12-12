from django import forms
from .models import CrmSystem

class CustomNumberInput(forms.widgets.NumberInput):
    input_type = 'text' 

class CrmSystemForm(forms.ModelForm):
    class Meta:
        model = CrmSystem
        fields = ['crm_name', 'crm_lastname', 'crm_number', 'crm_email', 'crm_password']
        widgets = {
            'crm_name': forms.TextInput(attrs={'class': 'firstName', 'required': True}),
            'crm_lastname': forms.TextInput(attrs={'class': 'lastName', 'required': True}),
            'crm_number': CustomNumberInput(attrs={'class': 'phoneNumber', 'required': True}),  # Используем кастомный виджет
            'crm_email': forms.EmailInput(attrs={'class': 'email', 'required': True}),
            'crm_password': forms.PasswordInput(attrs={'class': 'password', 'minlength': '8', 'required': True}),
        }

class CustomCrmSystemForm(CrmSystemForm):
    class Meta:
        model = CrmSystem
        fields = '__all__'  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['crm_email', 'crm_password']:
                field.required = False

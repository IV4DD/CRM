from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Payment, Patient



# class PaymentForm(ModelForm):
# 	class Meta:
# 		model = Payment
# 		fields = '__all__'

# class PatientForm(ModelForm):
# 	class Meta:
# 		model = Patient
# 		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

#Django Codemy
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'surname', 'middle_name', 'iin', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пациента'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию пациента'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите отчество пациента'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер сотового'}),
            'iin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ИИН'}),
        }		

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['income', 'payment_method', 'technical_cost', 'evening_shift', 'patient', 'doctor', 'procedurs']
        widgets = {
            'income': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите сумму'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите способ оплаты'}),
            'technical_cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите тех. затраты'}),
            'evening_shift': forms.CheckboxInput(),
            'patient': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Пациент'}),
            'doctor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Врач'}),            
            'procedurs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Процедура'}),
        }		


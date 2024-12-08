from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
	def clean_email(self):
		email = self.cleaned_data['email']

		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Este correo electrónico ya está registrado')
		return email



class ContactForm(forms.Form):
    email = forms.EmailField(label='Correo Electrónico', required=True, 
                              max_length=100, 
                              widget=forms.EmailInput(attrs={'class':'form-control',
                                                              'placeholder':'Introduzca su email'})) 
    name = forms.CharField(label="Nombre y Apellido",
                           required=True, min_length=5,
                           max_length=25,
                           widget=forms.TextInput(attrs={'class':'form-control',
                                                         'placeholder':'Introduzca sus Datos'}))
    message = forms.CharField(label='Mensaje', required=True,
                               widget=forms.Textarea(attrs={'class':'form-control',
                                                             'placeholder':'Escriba su mensaje aquí'}))
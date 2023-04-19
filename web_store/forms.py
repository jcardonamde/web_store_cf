from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, 
                            min_length=4, max_length=50,
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id': 'username',
                                'placeholder':'Ingresa tu usuario'
                            }))
    email = forms.EmailField(required=True,
                            widget=forms.EmailInput(attrs={
                                'class':'form-control',
                                'id': 'email',
                                'placeholder':'example@jonathancardona.com'
                            }))
    password = forms.CharField(required=True,
                            widget=forms.PasswordInput(attrs={
                                'class':'form-control',
                                'id': 'password'
                            }))
    password2 = forms.CharField(label='Confirmar Password',                 
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'
                                }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
    # Validate if the user exists
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')
        return username
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
    # Validate if the email user exists
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')
        return email
    
    
    # Override this method only if we need to validate fields or attributes that depend on each other
    def clean(self):
        cleaned_data = super().clean()
        
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'El password no coincide')
            

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class myCreateForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': "Hasło"}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': "Powtórz hasło"}))
    email = forms.CharField(max_length=20, widget=forms.EmailInput(attrs={'placeholder': "Email"}))
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Imię"}),
            'last_name': forms.TextInput(attrs={'placeholder': "Nazwisko"}),
            # 'email': forms.EmailInput(attrs={'placeholder': "Email"}),
        }

    def save(self, commit=True):
        user = super(myCreateForm, self).save(commit=False)
        user.username = user.email
        if commit:
            user.save()
        return user




from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()



class myLoginForm(forms.Form):
    email = forms.CharField(max_length=20, widget=forms.EmailInput(attrs={'placeholder': "Email"}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': "Hasło ss"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data['email']
        password1 = self.cleaned_data['password1']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'User {email} is empty in system.')
        user = User.objects.filter(email=email).first()
        if user:
            if not user.check_password1(password1):
                raise forms.ValidationError('Incorrect password1.')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['email', 'password1']


class myCreateForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': "Hasło"}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': "Powtórz hasło"}))
    email = forms.CharField(max_length=20, widget=forms.EmailInput(attrs={'placeholder': "Email"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Imię"}),
            'last_name': forms.TextInput(attrs={'placeholder': "Nazwisko"}),
        }
# qawsedrfZ123
    def save(self, commit=True):
        user = super(myCreateForm, self).save(commit=False)
        user.username = user.email
        if commit:
            user.save()
        return user

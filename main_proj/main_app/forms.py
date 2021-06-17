from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()



class myLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Hasło"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Nie udało się znaleźć konta z emailem {email}.')
        user = User.objects.filter(email=email).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Niepoprawne hasło')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "Email"})
        }


class myCreateForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Powtórz hasło"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Hasło"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Imię"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Nazwisko"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': "Email"}))

    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('@')[-1]
        if domain is None:
            raise forms.ValidationError("Niekorectny adress")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Uzytkownik istnieje')
        return email

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Rozne hasło')
        return self.cleaned_data

    class Meta:

        model = User
        fields = ['email', 'password', 'confirm_password', 'first_name', 'last_name']


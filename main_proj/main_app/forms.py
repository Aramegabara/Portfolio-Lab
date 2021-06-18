from django import forms

from .models import CustomUser, Donation , Category


class MyLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Hasło"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Nie udało się znaleźć konta z emailem {email}.')
        user = CustomUser.objects.filter(email=email).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Niepoprawne hasło')
        return self.cleaned_data

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "Email"})
        }


class MyCreateForm(forms.ModelForm):
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
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Uzytkownik istnieje')
        return email

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Rozne hasło')
        return self.cleaned_data

    class Meta:

        model = CustomUser
        fields = ['email', 'password', 'confirm_password', 'first_name', 'last_name']


class AddDonationForm(forms.ModelForm):
    categories = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1)
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=10)
    phone_number = forms.CharField(max_length=15)
    pick_up_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'mm/dd/yyyy'}), input_formats="MM/DD/YYYY")
    pick_up_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder':'--:-- --'}), input_formats="HH:MM AM/PM")
    pick_up_comment = forms.Textarea()

    class Meta:
        model = Donation
        fields = ['categories',
                  'quantity',
                  'address',
                  'city',
                  'zip_code',
                  'phone_number',
                  'pick_up_date',
                  'pick_up_time',
                  'pick_up_comment'
                  ]
        # test
#     # CHOICES = []
#     # categories = Category.objects.filter(name=)
#     # for category in categories:
#     #     CHOICES.append((category.id, category.name))
#     category = forms.CharField(widget=forms.RadioSelect())#, choices=CHOICES)
#
#     class Meta:
#         model = Category
#         fields = ['category']


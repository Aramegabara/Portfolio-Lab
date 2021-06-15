from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.db.models import Count, Sum
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth  import authenticate, login, logout

from .forms import myCreateForm, myLoginForm
from .models import *


class LandingPage(View):

    def get(self, request, *args, **kwargs):
        foundation = Institution.objects.all()
        bags = Donation.objects.aggregate(
            total=Sum('quantity'),
            institution=Count('pk')
        ),
        foundation_1 = foundation.filter(type='foundation')
        foundation_2 = foundation.filter(type='organization')
        foundation_3 = foundation.filter(type='local_donation')
        foundation = [foundation_1, foundation_2, foundation_3]
        p = Paginator(foundation, 1)
        page_num = request.GET.get('page', 1)
        page = p.page(page_num)
        context = {
            'page': page,
            'foundation': foundation,
            'total': bags[0]['total'],
            'institution': bags[0]['institution'],
        }
        return render(request, 'main_app/index.html', context)


class LandingPageListView(ListView):
    model = LandingPage
    template_name = "main_app/index.html"
    paginate_by = 2


class AddDonation(View):

    def get(self, request):
        return render(request, 'main_app/form.html')


class Login(View):

    def get(self, request):
        form = myLoginForm(request.POST or None)
        return render(request, 'main_app/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = myLoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            user = authenticate(email=email, password1=password1)
            if user:
                login(request, user)
        return HttpResponseRedirect('/')


class Register(View):

    def get(self, request):
        form = myCreateForm()
        return render(request, 'main_app/register.html', {'form': form})

    def post(self, request):
        form = myCreateForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request, 'Uzytkownik storzony' + user)
            return redirect('/login')
        else:
            errors = "Twoje hasło jest niepoprawne"
            # errors = [error_integ, error_val]
            return(request, 'main_app/regist.html', {'form': myCreateForm, 'errors': errors})



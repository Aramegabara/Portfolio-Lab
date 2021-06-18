from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.db.models import Count, Sum
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib.auth  import authenticate, login, logout

from .forms import MyCreateForm, MyLoginForm, AddDonationForm
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
        if bags[0]['total'] is None:
            bags[0]['total'] = 0
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
    paginate_by = 5


class AddDonation(View):

    def get(self, request, *args, **kwargs):
        form = AddDonationForm(request.POST or None)
        category = Category.objects.all()
        foundation = Institution.objects.all()
        institution = []
        for i in foundation:
            institution.append(i)
        content = {'category': category, 'institution': institution}
        return render(request, 'main_app/form.html', {'content': content, 'form': form})


class Login(View):

    def get(self, request, *args, **kwargs):
        form = MyLoginForm(request.POST or None)
        categories = Category.objects.all()
        donate = 'self.donat texst'
        context = {
            'form': form,
            'categories': categories,
            'donate': donate
        }
        return render(request, 'main_app/login.html', context)

    def post(self, request, *args, **kwargs):
        form = MyLoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')

        form = MyCreateForm()
        return render(request, 'main_app/register.html', {'form': form})


class Register(View):

    def get(self, request, *args, **kwargs):
        form = MyCreateForm(request.POST or None)
        content = {'form': form}
        return render(request, 'main_app/register.html', content)
    
    def post(self, request, *args, **kwargs):
        form = MyCreateForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('/login')
        else:
            return render(request, 'main_app/register.html', {'form': form})



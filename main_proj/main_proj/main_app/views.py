from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class BaseView(View):
    def get(self, request):
        return render(request, 'main_app/index.html')
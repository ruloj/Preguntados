from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required

@login_required
class HomeView(View):
    def get(self,request):
        render(request, 'questions/home.html')
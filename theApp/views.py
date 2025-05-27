from django.shortcuts import render
from django.contrib import auth
from django.views import View
from django.http import HttpResponse

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    

class ActivitiesView(View):
    def get(self, request):
        return render(request, 'activities.html')
    


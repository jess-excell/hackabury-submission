from django.shortcuts import render
from django.contrib import auth
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import addOn

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    
def submit_form(request):
    if request.method == 'POST':
        # save as session variables
        request.session["first_name"] = request.POST.get('first_name')
        request.session["last_name"] = request.POST.get('last_name')
        request.session[""]
        # then load new page which can check session variables (i hope)
        first_name = request.session.get("first_name")
        print(first_name)
        print("Last name:", request.POST.get('last_name'))
        print("From:", request.POST.get('from'))
        print("To:", request.POST.get('to'))
        print("Email:", request.POST.get('email'))
        return redirect("search")
    return HttpResponse("Invalid method", status=405)

def ActivitiesView(request):
    activities = addOn.objects.filter(type='activities', active=True)
    return render(request, 'activities.html', {'activities': activities})

class SearchView(View):
    def get(self, request):
        variables = {
            "first_name": request.session.get("first_name"),
            "last_name":  request.session.get("last_name")
        }
        
        return render(request, "search.html", variables)
from django.shortcuts import render
from django.contrib import auth
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    
def submit_form(request):
    if request.method == 'POST':
        # save as session variables
        
        
        request.session["first_name"] = request.POST.get('first_name')
        request.session["last_name"] = request.POST.get('last_name')
        request.session["from"] = request.POST.get('from')
        request.session["to"] = request.POST.get('to')
        request.session["departure"] = request.POST.get('departure')
        request.session["arrival"] = request.POST.get('arrival')
        request.session["number_of_travellers"] = request.POST.get('number of travellers')
        request.session["email"] = request.POST.get('email')
        
        request.session["airport_transfer"] = request.POST.get('airport_transfer')
        request.session["airport_fast_track"] = request.POST.get('airport_fast_track')
        request.session["airport_lounge"] = request.POST.get('airport_lounge')
        request.session["taxi"] = request.POST.get('taxi')
        request.session["insurance"] = request.POST.get('insurance')
        request.session["travel_money"] = request.POST.get('travel_money')
        request.session["activities_and_festivals"] = request.POST.get('activities_and_festivals')
        request.session["parking"] = request.POST.get('parking')
        
        
        return redirect("search")
    return HttpResponse("Invalid method", status=405)


class ActivitiesView(View):
    def get(self, request):
        return render(request, 'activities.html')

class SearchView(View):
    def get(self, request):
        
        params = {
            "first_name": request.session.get("first_name"),
            "last_name": request.session.get("last_name"),
            "from": request.session.get("from"),
            "to": request.session.get("to"),
            "departure": request.session.get("departure"),
            "arrival": request.session.get("arrival"),
            "number_of_travellers": request.session.get("number_of_travellers"),
            "email": request.session.get("email"),
            
            "airport_transfer": request.session.get("airport_transfer"),
            "airport_fast_track": request.session.get("airport_fast_track"),
            "airport_lounge": request.session.get("airport_lounge"),
            "taxi": request.session.get("taxi"),
            "insurance": request.session.get("insurance"),
            "travel_money": request.session.get("travel_money"),
            "activities_and_festivals": request.session.get("activities_and_festivals"),
            "parking": request.session.get("parking"),    
        }        
        return render(request, "search.html", params)
from django.shortcuts import render
from django.contrib import auth
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import addOn, HolidayPersonalityType
from django.db.models import Q
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

from django.views.generic.edit import FormView
#Renders homepage
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

#Submits the search information
def submit_form(request):
    print(request.method)
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

#Random activities page
def ActivitiesView(request):
    activities = addOn.objects.filter(type='activities', active=True)
    return render(request, 'activities.html', {'activities': activities})

#Search results
class SearchView(View):
    def get(self, request):
        
        #Look through addons , filter

        choices = [
            "transfer" if request.session.get("airport_transfer") == 'on' else None,
            "fasttrack" if request.session.get("airport_fast_track") == 'on' else None,
            "lounge" if request.session.get("airport_lounge") == 'on' else None,
            "taxi" if request.session.get("taxi") == 'on' else None,
            "insurance" if request.session.get("insurance") == 'on' else None,
            "airporthotel" if request.session.get("airport_hotel") == 'on' else None,
            "activities" if request.session.get("activities_and_festivals") == 'on' else None,
            "parking" if request.session.get("parking") == 'on' else None,
        ]
        
        testchoices = [item for item in choices if item is not None]
        # Clean up selected choices
        selected_types = [item for item in choices if item is not None]

        # Get locations from session
        from_location = request.session.get("from", "").strip().lower()
        to_location = request.session.get("to", "").strip().lower()

        # Filter addons by type and location (case-insensitive)
        results = addOn.objects.filter(
            type__in=selected_types,
            active=True
        ).filter(
            Q(location__iexact=from_location) | Q(location__iexact=to_location)
        )

        # Pass context to template
        context = {
            "results": results,
            "from": request.session.get("from"),
            "to": request.session.get("to"),
            "first_name": request.session.get("first_name"),
        }
        
        #Send data to page
        return render(request, 'search.html', context)
    
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    

class QuizView(FormView):
    """
    QuizView is a FormView (although currently missing a form class!)
    that handles the user's quiz answers and redirects the user to
    the personality page once they have answered all the questions.
    """
    def get(self, request):
        """Returns the template page to answer the quiz questions."""
        return render(request, 'quiz.html')
    
    def post(self, request, *args, **kwargs):
        """
        Handles the submission of quiz answers and redirects to the relevant personality
        page if quiz is successfully answered.
        """
        scores = {
            "traveller": 0,
            "lounger": 0,
            "thrill_seeker": 0,
            "artist": 0
        }
        
        answers = [ 
            request.POST.get("q1"),
            request.POST.get("q2"), 
            request.POST.get("q3")
        ]
        
        for answer in answers:
            match (answer):
                case "artist":
                    scores["artist"] += 1
                case "thriller":
                    scores["thrill_seeker"] += 1
                case "lounger":
                    scores["lounger"] += 1
                case "traveller":
                    scores["traveller"] += 1
                case None:
                    return HttpResponse("Invalid method", status=405)
        
        top = max(scores, key=scores.get)
        return redirect("personality", personality=top)

class PersonalityView(DetailView):
    """View used with `personality.html` to display user's personality type."""
    template_name = "personality.html"
    model = HolidayPersonalityType
    context_object_name="personality"
    slug_url_kwarg="personality"
    
    def get_context_data(self, **kwargs):
        """
        Adds the personality data to the context_data object to be used
        in `personality.html`.
        """
        data = super().get_context_data(**kwargs)
        data["personality"] = get_object_or_404(
            HolidayPersonalityType, 
            slug=self.kwargs.get("personality")
        )
        return data
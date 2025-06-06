from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('submit/', submit_form, name='submit_form'),
    path('search/', SearchView.as_view(), name="search"),
    path('activities/', ActivitiesView, name='activities'),
    path('about/', AboutView.as_view(), name='about'),
    path('quiz/', QuizView.as_view(), name="quiz"),
    path('personality/', PersonalitiesView.as_view(), name="personalities"),
    path('personality/<slug:personality>', PersonalityView.as_view(), name="personality")
]
from django.contrib import admin
from django.urls import path
from .views import HomeView, submit_form, SearchView, ActivitiesView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('submit/', submit_form, name='submit_form'),
    path('/search', SearchView.as_view(), name="search"),
    path('activities/', ActivitiesView, name='activities')
]
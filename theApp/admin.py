from django.contrib import admin
from .models import *

@admin.register(addOn)
class AddOnAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'availableFrom', 'availableTo', 'active')
    list_filter = ('type', 'active', 'location')
    search_fields = ('name', 'description', 'location')

admin.site.register(HolidayPersonalityType)
admin.site.register(ActivityType)
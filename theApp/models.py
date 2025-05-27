from django.db import models
'''
class customer(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    phonenumber = models.CharField(max_length=15, unique=True)
    startLocation = models.CharField(max_length=100, default='London')
    destination = models.CharField(max_length=100, blank=True)
    arrivaldate = models.DateField(null=True, blank=True)
    departuredate = models.DateField(null=True, blank=True)
    numberofpeople = models.IntegerField(default=1, max_length=20)


    travelinsurance = models.BooleanField(default=False, null=False, blank=False)
    outdooractivities = models.BooleanField(default=False, null=False, blank=False)
    transfer = models.BooleanField(default=False, null=False, blank=False)
    taxi = models.BooleanField(default=False, null=False, blank=False)
    travelmoney = models.BooleanField(default=False, null=False, blank=False)
    parking = models.BooleanField(default=False, null=False, blank=False)

    
    def __str__(self):
        return self.fname + " " + self.lname
    '''
    
class addOn (models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    availableFrom = models.DateField(null=False, blank=False)
    availableTo = models.DateField(null=False, blank=False)
    active = models.BooleanField(default=True, null=False, blank=False)
    type = models.CharField(max_length=50, choices=[
        ('activities', 'Activities'),
        ('transfer', 'Airport Transfer'),
        ('taxi', 'Taxi Services'),
        ('travelmoney', 'Travel Money'),
        ('parking', 'Parking Services'),
        ('insurance', 'Travel Insurance'),
        ('car', 'Car Hire'),
        ('fasttrack', 'Airport Fast Track'),
        ('lounge', 'Airport Lounge'),
    ], default='')
    location = models.CharField(max_length=100, blank=True)
    minTravelers = models.IntegerField(default=1)
    maxTravelers = models.IntegerField(default=1)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name
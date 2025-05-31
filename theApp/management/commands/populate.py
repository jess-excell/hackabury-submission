from django.core.management.base import BaseCommand
from datetime import date
from theApp.models import addOn, ActivityType, HolidayPersonalityType

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        """
        Creation script method to be run only on an empty database. Script adds sample data for:
        
        - Add ons
        - Activity types
        - Holiday personality types
        
        This script assumes that `py manage.py migrate` has already been run.
        \n**DO NOT RUN THIS IF THE DATABASE IS NOT EMPTY.**
        """
        
        if (addOn.objects.count() > 0):
            print("Error: Add on objects already exist. Population script must only be run on an empty database. Exiting.")
            return()
        
        if (ActivityType.objects.count() > 0):
            print("Error: Activity type objects already exist. Population script must only be run on an empty database. Exiting.")
            return()
        
        if (HolidayPersonalityType.objects.count() > 0):
            print("Error: Holiday personality type objects already exist. Population script must only be run on an empty database. Exiting.")
            return()
        
        print("Generating add on data...")
        add_on_sample_data = [
            {
                "name": "City Walking Tour",
                "description": "A guided walking tour through the city's historic landmarks.",
                "price": 29.99,
                "availableFrom": date(2025, 6, 1),
                "availableTo": date(2025, 12, 31),
                "active": True,
                "type": "activities",
                "location": "London",
                "minTravelers": 1,
                "maxTravelers": 10,
                "url": "https://example.com/walking-tour"
            },
            {
                "name": "Airport to Hotel Transfer",
                "description": "Private car transfer from the airport to your hotel.",
                "price": 45.00,
                "availableFrom": date(2025, 6, 1),
                "availableTo": date(2025, 12, 31),
                "active": True,
                "type": "transfer",
                "location": "Manchester",
                "minTravelers": 1,
                "maxTravelers": 4,
                "url": "https://example.com/airport-transfer"
            },
            {
                "name": "Travel Insurance Plan A",
                "description": "Comprehensive travel insurance for your trip.",
                "price": 18.50,
                "availableFrom": date(2025, 5, 1),
                "availableTo": date(2025, 12, 31),
                "active": True,
                "type": "insurance",
                "location": "",
                "minTravelers": 1,
                "maxTravelers": 10,
                "url": "https://example.com/insurance-a"
            },
            {
                "name": "Festival Entry Ticket",
                "description": "Entry ticket to the annual summer music festival.",
                "price": 55.00,
                "availableFrom": date(2025, 6, 10),
                "availableTo": date(2025, 6, 20),
                "active": True,
                "type": "activities",
                "location": "Leeds",
                "minTravelers": 1,
                "maxTravelers": 5,
                "url": "https://example.com/festival-ticket"
            },
            {
                "name": "Taxi from Station",
                "description": "Book a local taxi from the train station to your accommodation.",
                "price": 20.00,
                "availableFrom": date(2025, 5, 15),
                "availableTo": date(2025, 12, 31),
                "active": True,
                "type": "taxi",
                "location": "Liverpool",
                "minTravelers": 1,
                "maxTravelers": 4,
                "url": "https://example.com/taxi-station"
            },
            {
                "name": "Currency Exchange Voucher",
                "description": "Special rates for exchanging your currency.",
                "price": 0.00,
                "availableFrom": date(2025, 6, 1),
                "availableTo": date(2025, 9, 1),
                "active": True,
                "type": "travelmoney",
                "location": "Glasgow",
                "minTravelers": 1,
                "maxTravelers": 6,
                "url": "https://example.com/exchange"
            },
            {
                "name": "Airport Parking Space",
                "description": "Secure airport parking for the duration of your trip.",
                "price": 75.00,
                "availableFrom": date(2025, 5, 1),
                "availableTo": date(2025, 12, 31),
                "active": True,
                "type": "parking",
                "location": "Birmingham",
                "minTravelers": 1,
                "maxTravelers": 1,
                "url": "https://example.com/parking"
            },
            {
                "name": "Car Hire – Compact",
                "description": "Rent a compact car for your travel.",
                "price": 120.00,
                "availableFrom": date(2025, 6, 1),
                "availableTo": date(2025, 12, 31),
                "active": True,
                "type": "car",
                "location": "London",
                "minTravelers": 1,
                "maxTravelers": 4,
                "url": "https://example.com/compact-car"
            },
            {
                "name": "Airport Lounge Access",
                "description": "Relax in the airport lounge before your flight.",
                "price": 35.00,
                "availableFrom": date(2025, 5, 1),
                "availableTo": date(2025, 12, 31),
                "active": True,
                "type": "lounge",
                "location": "Heathrow",
                "minTravelers": 1,
                "maxTravelers": 6,
                "url": "https://example.com/lounge-access"
            },
            {
                "name": "Fast Track Security Pass",
                "description": "Skip the security queues at the airport.",
                "price": 12.00,
                "availableFrom": date(2025, 6, 1),
                "availableTo": date(2025, 12, 31),
                "active": True,
                "type": "fasttrack",
                "location": "Gatwick",
                "minTravelers": 1,
                "maxTravelers": 6,
                "url": "https://example.com/fasttrack"
            },
            {
                "name": "Zipline Adventure",
                "description": "Experience the thrill of ziplining over scenic landscapes.",
                "price": 50.00,
                "availableFrom": date(2025, 7, 1),
                "availableTo": date(2025, 9, 30),
                "active": True,
                "type": "activities",
                "location": "Lake District",
                "minTravelers": 1,
                "maxTravelers": 5,
                "url": "https://example.com/zipline"
            },
            {
                "name": "Scuba Diving Experience",
                "description": "Explore underwater life with guided scuba diving.",
                "price": 95.00,
                "availableFrom": date(2025, 6, 1),
                "availableTo": date(2025, 8, 31),
                "active": True,
                "type": "activities",
                "location": "Cornwall",
                "minTravelers": 2,
                "maxTravelers": 6,
                "url": "https://example.com/scuba"
            },
            {
                "name": "Evening River Cruise",
                "description": "Enjoy dinner and views on a riverboat.",
                "price": 65.00,
                "availableFrom": date(2025, 5, 10),
                "availableTo": date(2025, 9, 10),
                "active": True,
                "type": "activities",
                "location": "York",
                "minTravelers": 1,
                "maxTravelers": 8,
                "url": "https://example.com/river-cruise"
            },
            {
                "name": "Weekend Festival Pass",
                "description": "Access to all events over the weekend festival.",
                "price": 120.00,
                "availableFrom": date(2025, 6, 20),
                "availableTo": date(2025, 6, 22),
                "active": True,
                "type": "activities",
                "location": "Brighton",
                "minTravelers": 1,
                "maxTravelers": 6,
                "url": "https://example.com/festival-pass"
            },
            {
                "name": "Theatre Show Ticket",
                "description": "Front-row seats to a West End performance.",
                "price": 89.99,
                "availableFrom": date(2025, 5, 1),
                "availableTo": date(2025, 12, 1),
                "active": True,
                "type": "activities",
                "location": "London",
                "minTravelers": 1,
                "maxTravelers": 2,
                "url": "https://example.com/theatre"
            },
            {
                "name": "Snowdonia Hiking Guide",
                "description": "Guided hike across Snowdonia National Park.",
                "price": 40.00,
                "availableFrom": date(2025, 6, 15),
                "availableTo": date(2025, 9, 15),
                "active": True,
                "type": "activities",
                "location": "Wales",
                "minTravelers": 2,
                "maxTravelers": 10,
                "url": "https://example.com/hiking"
            },
            {
                "name": "Kayaking Session",
                "description": "1-hour guided kayaking on calm waters.",
                "price": 35.00,
                "availableFrom": date(2025, 7, 1),
                "availableTo": date(2025, 9, 30),
                "active": True,
                "type": "activities",
                "location": "Bath",
                "minTravelers": 1,
                "maxTravelers": 4,
                "url": "https://example.com/kayaking"
            },
            {
                "name": "Cooking Class",
                "description": "Learn to cook authentic local dishes.",
                "price": 70.00,
                "availableFrom": date(2025, 6, 5),
                "availableTo": date(2025, 11, 30),
                "active": True,
                "type": "activities",
                "location": "Oxford",
                "minTravelers": 1,
                "maxTravelers": 6,
                "url": "https://example.com/cooking"
            },
            {   
                "name": "Ghost Tour",
                "description": "A spooky night-time tour of haunted sites.",
                "price": 25.00,
                "availableFrom": date(2025, 10, 1),
                "availableTo": date(2025, 10, 31),
                "active": True,
                "type": "activities",
                "location": "Edinburgh",
                "minTravelers": 1,
                "maxTravelers": 5,
                "url": "https://example.com/ghost-tour"
            },
            {
                "name": "Museum Day Pass",
                "description": "Unlimited entry to multiple museums in the city.",
                "price": 22.00,
                "availableFrom": date(2025, 5, 1),
                "availableTo": date(2025, 12, 31),
                "active": True,
                "type": "activities",
                "location": "Cambridge",
                "minTravelers": 1,
                "maxTravelers": 6,
                "url": "https://example.com/museum-pass"
            }
        ]
        
        print("Done.")
        print("Populating add ons...")
        
        for entry in add_on_sample_data:
            addOn.objects.create(**entry)
        
        print("Done.")
        
        print("Creating and populating activities...")
        activity_sample_data = [
            {
                "name": "Hiking",
                "description": "HIKING DESCRIPTION",
                "image_src": "https://images.pexels.com/photos/1365425/pexels-photo-1365425.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            },
            {
                "name": "Kayaking",
                "description": "KAYAKING DESCRIPTION",
                "image_src": "https://images.pexels.com/photos/933843/pexels-photo-933843.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            },
            {
                "name": "Beach Weekend",
                "description": "BEACH DESCRIPTION",
                "image_src": "https://images.pexels.com/photos/189349/pexels-photo-189349.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            },
            {
                "name": "Cooking Class",
                "description": "COOKING DESCRIPTION",
                "image_src": "https://images.pexels.com/photos/2284166/pexels-photo-2284166.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            },
            {
                "name": "Theatre",
                "description": "THEATRE DESCRIPTION",
                "image_src": "https://images.pexels.com/photos/1714361/pexels-photo-1714361.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            },
            {
                "name": "Bungee Jumping",
                "description": "BUNGEE DESCRIPTION",
                "image_src": "https://images.pexels.com/photos/1486036/pexels-photo-1486036.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            },
            {
                "name": "Ziplining",
                "description": "ZIPLINING DESCRIPTION",
                "image_src": "https://images.pexels.com/photos/6663059/pexels-photo-6663059.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            },
            {
                "name": "Racing",
                "description": "RACING DESCRIPTION",
                "image_src": "https://images.pexels.com/photos/12795/pexels-photo-12795.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            }
        ]
        
        for entry in activity_sample_data:
            ActivityType.objects.create(**entry)
        print("Done.")
        
        print("Creating and populating Holiday Personality types...")
        
        temp = HolidayPersonalityType.objects.create(
            slug="artist",
            description="The artist loves to look at paintings i guess",
            image_src="https://images.unsplash.com/photo-1653987255814-3b4c05832660?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )
        
        temp.recommended_activities.set([
            ActivityType.objects.get(name="Theatre"),
            ActivityType.objects.get(name="Cooking Class")
        ])
    
        temp = HolidayPersonalityType.objects.create(
            slug="traveller",
            description="Courageous and curious, the traveller loves to explore and try new things. The unknown doesn't deter you, it excites you.",
            image_src="https://images.unsplash.com/photo-1505778276668-26b3ff7af103?q=80&w=1161&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )
        
        temp.recommended_activities.set([
            ActivityType.objects.get(name="Hiking"),
            ActivityType.objects.get(name="Kayaking")
        ])
        
        temp = HolidayPersonalityType.objects.create(
            slug="thrill_seeker",
            description="Exciting, outgoing and bold, the thrill seeker loves to seek out new adventures.",
            image_src="https://images.unsplash.com/photo-1601224748193-d24f166b5c77?q=80&w=1064&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )
        
        temp.recommended_activities.set([
            ActivityType.objects.get(name="Bungee Jumping"),
            ActivityType.objects.get(name="Ziplining"),
            ActivityType.objects.get(name="Racing")
        ])
        
        temp = HolidayPersonalityType.objects.create(
            slug="lounger",
            description="Calm and reliable, the lounger loves a more relaxing holiday.",
            image_src="https://images.unsplash.com/photo-1560332944-d047e59ac9b2?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        )
        
        temp.recommended_activities.set([
            ActivityType.objects.get(name="Beach Weekend"),
            ActivityType.objects.get(name="Cooking Class"),
            ActivityType.objects.get(name="Theatre")
        ])
    
        print("Done.")
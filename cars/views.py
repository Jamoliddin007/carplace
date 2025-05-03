from django.shortcuts import render
from cars.models import Car
from users.models import CustomUser

def index(request):
    cars = Car.objects.all()
    users = CustomUser.objects.filter(
        is_active=True,
        is_staff=True,
        is_superuser=False
    )
    testimonials = CustomUser.objects.filter(
        is_active=True,
        is_staff=False,
        is_superuser=False
    )   


    return render(
        request=request,
        template_name='index.html',
        context={
            "cars":cars,
            "users":users,
            "testimonials":testimonials    
        }
    )

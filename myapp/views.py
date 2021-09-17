from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    countries = Country.objects.all()
    return render(request, 'myapp/index.html', {'countries':countries})

def load_state(request):
    country_id = request.GET.get('country')                        #-------get current country id
    states = State.objects.filter(country_id=country_id).order_by('name')   #------get state with respct to country id
    return render(request, 'myapp/state_dropdown.html', {'states': states})

def load_city(request):
    state_id = request.GET.get('state')                            #------get current state id
    cities = City.objects.filter(state_id=state_id).order_by('name')    #------get city with respct to state id
    return render(request, 'myapp/city_dropdown.html', {'cities': cities})



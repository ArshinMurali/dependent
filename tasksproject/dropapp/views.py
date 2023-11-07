from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *

def dependantfield(request):

    countryid = request.GET.get('country', None)
    stateid = request.GET.get('state', None)
    state = None
    district = None
    if countryid:
        getcountry = Country.objects.get(id=countryid)
        state = State.objects.filter(country=getcountry)
    if stateid:
        getstate = State.objects.get(id=stateid)
        district = District.objects.filter(state=getstate)
    country = Country.objects.all()



    return render(request, 'dependantfield.html', locals())

def get_states(request):
    country_id = request.GET['country_id']
    get_country = Country.objects.get(id=country_id)
    state = State.objects.filter(country=get_country)
    return render(request, 'get-states.html', locals())

def last(request):
    return render(request,'submit.html')


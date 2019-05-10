from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices
# Importing the choice dictionaries from listings/choices.py

from listings.models import Listing
from realtors.models import Realtor
# from the listing application model we want to import the Listing model

# Create your views here.


def index(request):
    # return HttpResponse('<h1>Sup Jude</h1>')
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    # Assign Listings to the Listing model, order des by list date, show only published listings, and limit the results to 3

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    # Passing the listings into 'pages/index.html'; after this, go to 'pages.index.html' to loop through the dictonary of listings passed into that page as part of this response
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all Realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP, in case the client wants more than one to be recognized
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)

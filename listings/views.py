from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
# Importing the choices dictionaries to load into listings/search.html
# Since we're already in the listings app we can simply use .choices


# fetching data for passing into view
from .models import Listing


def index(request):
    # Create a dictionary to be passed in as a second parameter for the view templating engine
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        "listings": paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # Passing in the model and primary key
    # If a Listing with that ID is not foudn, return 404
    # listing_id is passed in through the url in listings/urls.py
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # the values in '' below == the name field of the select dropdown in the search form

    # Search description for keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # Search for city, case insensitive.
    # for case sensitive use 'exact' instead of 'iexact'
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    # Search for state, case insensitive.
    # for case sensitive use 'exact' instead of 'iexact'
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)

    # Search for bedroom, case insensitive.
    # lte == less than or equal to, so up to the number put in
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)

    # Search for bedroom, case insensitive.
    # lte == less than or equal to, so up to the number put in
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    # Set this up later with results pagination
    #paginator = Paginator(listings, 3)
    #page = request.GET.get('page')
    #paged_listings = paginator.get_page(page)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
        # 'values' included to have form field selections persist
    }
    return render(request, 'listings/search.html', context)

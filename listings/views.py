from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
    return render(request, 'listings/search.html')

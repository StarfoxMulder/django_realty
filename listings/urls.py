from django.urls import path

from . import views

# These will apply to the path AFTER /listings
# path('') will be '/listings'
# path('<int:listing_id>') will be '/listings/22' or whatever the listing_is integer is for that listing record
# path('/search') will be '/listings/search'


urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    # url endpoint, the method you want attached to that endpont, name to easily access this path
]

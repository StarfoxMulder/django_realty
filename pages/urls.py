from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
    # url endpoint, the method you want attached to that endpont, name to easily access this path
]

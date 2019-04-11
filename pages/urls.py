from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
    # url endpoint, the method you want attached to that endpont, name to easily access this path
]

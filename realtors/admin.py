from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_per_page = 20

    # Register your models here. This adds them to the admin panel site administration
admin.site.register(Realtor, RealtorAdmin)

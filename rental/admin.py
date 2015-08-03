from django.contrib import admin

from .models import Rental


class RentalAdmin(admin.ModelAdmin):
    search_fields = ['who', 'what']
    list_display = ['who', 'what', 'when']


admin.site.register(Rental, RentalAdmin)

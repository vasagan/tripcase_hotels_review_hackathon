from django.contrib import admin


# Register your models here.

from .models import *

class Hotel_Admin(admin.AdminSite):
    site_header = 'Sabre Hotels Admin Panel'

class WifiAdmin(admin.ModelAdmin):
    list_display = ['property_id', 'name', 'url', 'full_address','expected_speed', 'percentile_rank','confidence']


admin_site = Hotel_Admin(name='Sabre Hotels Admin Panel')
admin_site.register(hotel_wifi_strength, WifiAdmin)


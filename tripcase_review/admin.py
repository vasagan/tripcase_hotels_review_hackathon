from django.contrib import admin

# Register your models here.
from .models import *
from wifi_test.admin import admin_site

class TripcaseAdmin(admin.ModelAdmin):
    list_display = ['property_id', 'guest_name', 'star_rating','guest_review', 'device_type']




admin_site.register(tripcase_review, TripcaseAdmin)
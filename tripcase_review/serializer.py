from rest_framework import serializers
from .models import *
from .views import *
from django.core import exceptions



class TripcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = tripcase_review
        fields = ['property_id', 'star_rating', 'guest_review', 'guest_name', 'device_type']






from rest_framework import serializers
from .models import *

class WifiSerializer(serializers.ModelSerializer):
    class Meta:
        model = hotel_wifi_strength
        fields = '__all__'

from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


class tripcase_review(models.Model):
    property_id = models.IntegerField()
    star_rating = models.IntegerField()
    guest_review = models.TextField()
    guest_name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)

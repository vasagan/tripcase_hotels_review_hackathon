from django.db import models

# Create your models here.


class hotel_wifi_strength(models.Model):
    property_id = models.IntegerField(unique=True)
    ean_id = models.IntegerField()
    tripadvisor_id = models.IntegerField()
    name = models.CharField(max_length=200)
    url = models.URLField()
    full_address = models.TextField()
    expected_speed = models.CharField(max_length=30)
    percentile_rank = models.CharField(max_length=30)
    confidence = models.CharField(max_length=30)

    def __str__(self):
        return self.name


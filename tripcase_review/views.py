from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework import generics, viewsets, serializers, permissions
from .serializer import *
from django.core.mail import send_mail
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from django.db.models import Avg, Max, Min
from wifi_test.models import hotel_wifi_strength


# Create your views here.

@api_view(['GET', 'POST'])
def save_message(request):
    if request.method == 'POST':
        property_id = request.data['property_id']
        star_rating = request.data['star_rating']
        guest_review = request.data['guest_review']
        guest_name = request.data['guest_name']
        device_type = request.data['device_type']

        str = "test success"

        return Response({"message": str })
    return Response({
        "status": "success", # success or failure
    })



class SaveMessage(generics.CreateAPIView):
    serializer_class = TripcaseSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return tripcase_review.objects.all()



@api_view(['GET'])
def property_rating(request, property_number):
    """
    A view that returns the count of active users in JSON.
    """
    reviewers_count = tripcase_review.objects.filter(property_id=property_number).count()
    rating = tripcase_review.objects.filter(property_id=property_number).aggregate(Avg('star_rating'))
    content = {'rating': rating['star_rating__avg'], 'total_reviews': reviewers_count }
    if hotel_wifi_strength.objects.filter(property_id=property_number).exists():
        prop = hotel_wifi_strength.objects.get(property_id=property_number)
        wifi_details = { 'property_id': prop.property_id, 'property name': prop.name, 'address': prop.full_address, 'url': prop.url, 'wifi speed': prop.expected_speed, 'wifi rank': prop.percentile_rank, 'rating': rating['star_rating__avg'], 'total_reviews': reviewers_count }
        return Response(wifi_details)
    return Response(content)



@api_view(['GET'])
def property_review(request, property_number):
    """
    A view that returns the count of active users in JSON.
    """
    all_reviews = tripcase_review.objects.filter(property_id=property_number).all().order_by('star_rating')
    review_list =[]
    for review in all_reviews:
        review_list.append(
            {
                'rating': review.star_rating,
                'guest_name': review.guest_name,
                'device_type': review.device_type,
                'guest_review': review.guest_review
            }
        )
    if hotel_wifi_strength.objects.filter(property_id=property_number).exists():
        prop = hotel_wifi_strength.objects.get(property_id=property_number)
        wifi_details = { 'property_id': prop.property_id, 'ean id': prop.ean_id, 'tripadvisor id': prop.tripadvisor_id, 'property name': prop.name, 'address': prop.full_address, 'url': prop.url, 'wifi speed': prop.expected_speed, 'wifi rank': prop.percentile_rank }
        wifi_details =  { 'wifi_rank': wifi_details, 'reviews': review_list }
        return Response(wifi_details)
    review_list = {'reviews': review_list}
    return Response(review_list)
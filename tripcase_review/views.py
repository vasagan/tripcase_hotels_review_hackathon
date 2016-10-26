from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework import generics, viewsets, serializers, permissions
from .serializer import *
from django.core.mail import send_mail
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
"""
    def  perform_create(self, serializer):
        serializer.save()
        send_mail('Test Email', 'Here is the message.', 'vasagan@orgbasket.com',['vasagant@gmail.com'], fail_silently=False)
"""
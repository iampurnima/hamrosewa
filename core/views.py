from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ServiceProvider, Booking, ServiceCategory, Review
from .serializers import (
    ServiceProviderSerializer, 
    BookingSerializer, 
    ServiceCategorySerializer, 
    ReviewSerializer
)
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.models import User


# Test API to confirm connection
class TestAPI(APIView):
    def get(self, request):
        # Dummy data to test the connection
        dummy_data = {
            "id": 1,
            "user": "test_user",
            "service": "Electrician",
            "review": "Great service!",
            "rating": 5,
            "created_at": "2024-11-20T10:00:00Z"
        }
        return Response(dummy_data, status=status.HTTP_200_OK)


# List and Create Service Providers
class ServiceProviderList(ListCreateAPIView):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer


# List Service Categories
class ServiceCategoryList(APIView):
    def get(self, request):
        categories = ServiceCategory.objects.all()
        serializer = ServiceCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Create a Booking
class BookingList(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Submit a Review
class ReviewList(APIView):
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

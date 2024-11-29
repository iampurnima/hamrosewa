from rest_framework import serializers
from .models import ServiceProvider, Booking, ServiceCategory, Review

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'

class ServiceProviderSerializer(serializers.ModelSerializer):
    # services = ServiceCategorySerializer(many=True)

    class Meta:
        model = ServiceProvider
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

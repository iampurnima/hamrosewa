# from django.urls import path
# from .views import ServiceProviderList, BookingList, ReviewList, TestAPI

# urlpatterns = [
#     path('providers/', ServiceProviderList.as_view(), name='provider-list'),
#     path('bookings/', BookingList.as_view(), name='booking-list'),
#     path('reviews/', ReviewList.as_view(), name='review-list'),
#     path('test/', TestAPI.as_view(), name='test-view'),
# ]

from django.urls import path
from .views import ServiceProviderList, BookingList, ReviewList, ServiceCategoryList

urlpatterns = [
    path('api/providers/', ServiceProviderList.as_view(), name='provider-list'),
    path('api/bookings/', BookingList.as_view(), name='booking-list'),
    path('api/reviews/', ReviewList.as_view(), name='review-list'),
    path('api/categories/', ServiceCategoryList.as_view(), name='category-list'),
    
]

from django.contrib import admin
from .models import ServiceProvider
from .models import ServiceCategory
from .models import Review
from .models import Booking
# Register your models here.
admin.site.register(ServiceCategory)
admin.site.register(ServiceProvider)
admin.site.register(Review)
admin.site.register(Booking)
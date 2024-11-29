from django.db import models
from django.contrib.auth.models import User

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=200)
    service = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, null=True)
    verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='provider_pictures/', blank=True, null=True)
    ratings = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Completed', 'Completed')],
        default='Pending'
    )

    def __str__(self):
        return f"Booking by {self.user.username} with {self.provider.user.username} completed at {self.time}."

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.provider.user.username}"

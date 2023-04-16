from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    """Expand the User model with additional fields."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.TextField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location_x = models.CharField(max_length=30, blank=True, null=True)
    location_y = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        """Dunder method to return the username of the user."""
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a user profile when a user is created. Receiver for the post_save signal from User model."""
    if created:
        UserProfile.objects.create(user=instance)

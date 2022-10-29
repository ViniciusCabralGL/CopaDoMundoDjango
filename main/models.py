from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False


class LoginLevel(models.Model):
    # sub table for level to get the access in the system
    name = models.CharField(max_length=255, blank=False, null=False)
    value = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name


class UserLogin(models.Model):
    # User and Password with the access
    name = models.CharField(max_length=255, blank=False, null=False)
    level = models.ForeignKey(LoginLevel, related_name="level", on_delete=models.CASCADE)
    idUserFK = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    activated = models.BooleanField(default=False)
    firstAccess = models.BooleanField(default=True)
    image = models.ImageField(upload_to=upload_image_area_map, blank=True, null=True)

    def __str__(self):
        return self.name

    def upload_image_area_map(self, filename):
        return f"images/maps/{filename}"

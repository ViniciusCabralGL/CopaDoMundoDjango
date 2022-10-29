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


def upload_user_image(self, filename):
        return f"images/maps/{filename}"


class UserLogin(models.Model):
    # User and Password with the access
    name = models.CharField(max_length=255, blank=False, null=False)
    level = models.ForeignKey(LoginLevel, related_name="level", on_delete=models.CASCADE, blank=False, null=False)
    idUserFK = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, blank=False, null=False)
    activated = models.BooleanField(default=True)
    firstAccess = models.BooleanField(default=True)
    image = models.ImageField(upload_to=upload_user_image, blank=True, null=True)

    def __str__(self):
        return self.name


class Selecao(models.Model):
    # Team
    class Suit(models.IntegerChoices):
        OPTION1 = 23
        OPTION2 = 24
        OPTION3 = 25
        OPTION4 = 26

    nome = models.CharField(max_length=255, blank=False, null=False)
    qtdJogadores = models.IntegerField(choices=Suit.choices)

    def __str__(self):
        return self.nome
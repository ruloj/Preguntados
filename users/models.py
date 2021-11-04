from django.db import models
from django.contrib.auth.models import AbstractUser

"""
username
nombre
apellido
contraseña
correo

foto
sobre mi
"""

class PreguntadosUser(AbstractUser):
    """ Custom User Model """
    about_me = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(blank=True)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    # email = models.EmailField()
    # password = models.CharField(max_length=20)
    ROLE_CHOICES = [
        ("admin", 'Admin'),
        ("user", 'User'),
        ("staff", 'Staff'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    def __str__(self):
            return f"{self.name} ({self.role})"

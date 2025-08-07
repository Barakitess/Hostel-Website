from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20)
    room_no = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        ADMIN = "ADMIN", "Admin"
        WARDEN = "WARDEN", "Warden"
        HMC = "HMC", "Hostel Management Committee"

    # Role field
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT
    )

    # Extra fields for Students
    roll_no = models.CharField(max_length=20, blank=True, null=True)
    hostel_room_no = models.CharField(max_length=10, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)

    def _str_(self):
        return f"{self.username} ({self.role})"
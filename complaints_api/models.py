from django.db import models

COMPLAINT_TYPES = [
    ('carpentry', 'Carpentry'),
    ('electricity', 'Electricity'),
    ('plumbing', 'Plumbing'),
    ('sanitary', 'Sanitary'),
    ('civil', 'Other Civil Works'),
]


class Complaint(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    room_number = models.CharField(max_length=10)
    complaint_type = models.CharField(max_length=20, choices=COMPLAINT_TYPES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint #{self.id} - {self.complaint_type}"

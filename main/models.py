from zoneinfo import available_timezones
from django.db import models
from django.contrib.auth.models import User

HOSTEL_CHOICES = (
    ('hostel-1','Hostel-1'),
    ('hostel-2', 'Hostel-2'),
    ('hostel-3','Hostel-3'),
)

class User_info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    hostel_name = models.CharField(max_length=10)
    room = models.CharField(max_length=10)


class Complaint(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    hostel_name = models.CharField(max_length=200)
    room = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)
    status = models.CharField(max_length=50, default="pending")

    category = models.CharField(max_length=200)
    availability = models.DateTimeField()
    officer = models.CharField(max_length=9)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.person + "\n" + self.hostel_name + "\n" + self.officer + "\n" + self.category + "\n" + self.description
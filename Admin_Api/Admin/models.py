from django.db import models
from django.utils import timezone

def user_file_storage(instance, filename):
    # Define the upload path for the file
    return f'uploads/user_{instance.user_id}/{filename}'

# Create your models here.
class AdminUser(models.Model):
    phno = models.CharField(max_length=10,primary_key=True)
    admin_type = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stauts = models.CharField(max_length=10)


class AdminDetails(models.Model):
    salutation = models.CharField(max_length=6)
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    district = models.CharField(max_length=12)
    subdiv = models.CharField(max_length=12)
    block = models.CharField(max_length=12)
    address = models.CharField(max_length=64)
    dob = models.DateField(blank=True)
    doc = models.FileField(upload_to=user_file_storage)

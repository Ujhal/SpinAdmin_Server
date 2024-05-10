from django.db import models
from django.core.validators import FileExtensionValidator
from divisions.helpers import check_block, check_district, check_subdivision
from .helpers import check_type
from django.utils import timezone


def cfile(instance, filename):
    return ''.join(['temp/', str(instance.phone_number), '.', filename.split('.')[-1]])


# Create your models here.
class User(models.Model):
    phone_number = models.CharField(max_length=10, primary_key=True)
    salutation = models.CharField(max_length=6)
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    email = models.EmailField(max_length=64, blank=True)
    district = models.CharField(max_length=12, validators=[check_district])
    subdiv = models.CharField(max_length=12, validators=[check_subdivision])
    block = models.CharField(max_length=12, validators=[check_block])
    address = models.CharField(max_length=64)
    dob = models.DateField(blank=True)

    dtype = models.CharField(max_length=3, validators=[
        check_type])
    doc = models.FileField(upload_to=cfile, null=True, blank=True, validators=[
                           FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png'])])
    status = models.CharField(max_length=10,default='processing')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    remarks = models.CharField(max_length=30,null= True)
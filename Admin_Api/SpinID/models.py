from django.db import models

# Create your models here.
class Spinid(models.Model):
    spinid = models.CharField(max_length=14)
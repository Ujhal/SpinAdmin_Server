from django.contrib import admin
from .models import AdminDetails, AdminUser

# Register your models here.
admin.site.register(AdminUser)
admin.site.register(AdminDetails)
from .models import Profile
from django.contrib import admin

# Register your models here.
register = admin.site.register
register(Profile)

from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list = ["user"]

admin.site.register(Profile, ProfileAdmin)
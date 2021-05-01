from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=255, blank=True)
	contact = models.CharField(max_length=20, blank=True)
	photo = models.ImageField(upload_to='images/profile/', null=True, blank=True)

	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

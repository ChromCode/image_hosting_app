from __future__ import unicode_literals

from django.db import models

# Create your models here

class User_Image(models.Model):
	is_public = models.BooleanField(default=False)
	image = models.ImageField(upload_to='images/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.image.url

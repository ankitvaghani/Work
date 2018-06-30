from django.db import models

# Create your models here.

class userInfo(models.Model):
	"""docstring for userInfo"""
	user_name = models.CharField(max_length=100)
	user_email = models.CharField(max_length=100)
	user_pass = models.CharField(max_length=100)	
	user_mobile = models.CharField(max_length=10)
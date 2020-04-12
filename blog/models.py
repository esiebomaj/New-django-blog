from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class post(models.Model):
	title=models.CharField(max_length=200)
	author=models.ForeignKey(to=User, on_delete=models.CASCADE,)
	content=models.TextField()
	date_created=models.DateField(auto_now=True)

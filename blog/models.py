from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class post(models.Model):
	title=models.CharField(max_length=200)
	author=models.ForeignKey(to=User, on_delete=models.CASCADE,)
	content=models.TextField()
	date_created=models.DateField(auto_now=True)

	def __str__(self):
		return self.title



	def get_absolute_url(self):
		return reverse('post-detail', args=[str(self.id)])

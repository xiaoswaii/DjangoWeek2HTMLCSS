from django.db import models
from django.conf import settings

class Text(models.Model):
	user=models.CharField(max_length=20, blank=False)
	talk = models.CharField(max_length=50, blank=True)
	def _str_(self):
		return self.user + "" + self.talk

#class Day(models.Model):
#	libai=models.CharField(max_length=20,blank=False)
#	def _str_(self):
#		return self.libai
# Create your models here.

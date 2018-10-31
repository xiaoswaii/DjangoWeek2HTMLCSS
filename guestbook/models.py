from django.db import models
from django.conf import settings

class Msg(models.Model):
	#user=models.CharField(max_length=20, blank=False)
	talk = models.CharField(max_length=50, blank=True)
	sender=models.CharField(max_length=50,blank=False,default="null")
	receiver=models.CharField(max_length=50,blank=False , default="null")
	date_time=models.DateTimeField()
	def _str_(self):
		return self.sender + "" + self.talk + "" + self.date_time + "" + self.receiver

#class Day(models.Model):
#	libai=models.CharField(max_length=20,blank=False)
#	def _str_(self):
#		return self.libai
# Create your models here.

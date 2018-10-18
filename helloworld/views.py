from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import Text
import datetime

def index(request):
	return render(request, 'index.html')

def guestbook(request):
	if request.method=='POST':
		user=request.POST['user']
		talk=request.POST['talk']
		date_time=datetime.datetime.now()
		conversation=Text.objects.create(user=user, talk=talk,date_time=date_time)
		conversation=Text.objects.all()
	conversation=Text.objects.all()
	return render(request, 'guestbookver1.html',locals())

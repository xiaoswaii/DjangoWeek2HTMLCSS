from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import Text
def index(request):
	if request.method=='POST':
		user=request.POST['user']
		talk=request.POST['talk']
		conversa=Text.objects.create(user=user, talk=talk)
		conversation=Text.objects.all()
	return render(request, 'guestbookver1.html',locals())

def p2(request):
	return render(request,'p2.html')

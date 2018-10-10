from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import TextMessage
def index(request):

	talk1 = TextMessage.objects.create(talker='Xiaoswaii',message='Hello,littleyang!' )
	talk2 = TextMessage.objects.create(talker='Littleyang',message='Hello,xiaoswaii')
	msgs=TextMessage.objects.all()
	return render(request, 'guestbookver1.html',locals())

#def p2(request):
#	return render(request,'p2.html',locals())

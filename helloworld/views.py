from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
	talk=["Hello","idiot","what r you doing"]
	return render(request, 'guestbookver1.html',{'talk':talk})

def p2(request):
	day=["一","二","三","四","五"]
	return render(request,'p2.html',{'day':day})

from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import Text
import datetime

def index(request):
	if request.user.is_authenticated:
		name=request.user.username
	return render(request, 'index.html')

def register(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		email=request.POST['email']
		firstname=request.POST['firstname']
		lastname=request.POST['lastname']
		try:
			user = User.objects.get(username=username)
		except:
			user=None
		
		if user is not None:
			message="Username used by another"
		else:
			user=User.objects.create_user(username ,email, password )
			user.first_name=firstname
			user.last_name=lastname
			user.save()
			message="You Had Registered Succeessfully!"
			return render(request , "index.html",locals())
	return render(request , "register.html",locals()) 

def login(request):
	if request.user.is_authenticated:
		return redirect('/index/')
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user=auth.authenticate(username=username,password=password)
	if user is not None and user.is_active:
		auth.login(request,user)
		message='登入成功'
		return redirect('/index')
		
	else:
		message='尚未登入'
		return render(request,"login.html",locals())
	"""if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:         #若驗證成功，以 auth.login(request,user) 登入
				if user.is_active:
					auth.login(request,user)
					return redirect('/index/')  #登入成功產生一個 Session，重導到<index.html>
					message = '登入成功!'
				else:
					message = '帳號尚未啟用!'
		else:
				message = '登入失敗!'
	return render(request,"login.html",locals())"""

def logout(request):
	auth.logout(request)  #登出成功清除 Session，重導到<index.html>
	return redirect('/index/')

def guestbook(request):
	if request.user.is_authenticated:
		name=request.user.username
	else:
		message="你尚未登入"
	if request.method=='POST':
		user=request.POST['user']
		talk=request.POST['talk']
		date_time=datetime.datetime.now()
		conversation=Text.objects.create(user=user, talk=talk,date_time=date_time)
		conversation=Text.objects.all()
	conversation=Text.objects.all()
	return render(request, 'guestbookver1.html',locals())

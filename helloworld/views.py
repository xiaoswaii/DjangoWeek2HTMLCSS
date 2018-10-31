from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import Msg
import datetime

def listuser(request):
	if 'talkto' in request.POST:
		sender=request.user.username
		receiver=request.POST['receiver']
		conversation=Msg.objects.filter(receiver=receiver)
		return render(request,'guestbookver1.html',locals())
	if 'search' in request.POST:
		searchname=request.POST['searchname']
		namelist=User.objects.filter(username__contains=searchname)
		return render(request,'listuser.html',locals())
        #namelist=User.objects.all()
	'''if 'delete' in request.POST:
		username=request.POST['username']
		User.objects.filter(username=username).delete()'''
	namelist=User.objects.all()
	return render(request,'listuser.html',locals())

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
		sender=request.user.username
	else:
		message="你尚未登入"

	if 'searching' in request.POST:
		talk=request.POST['talk']
		receiver=request.POST['receiver']
		conversation=Msg.objects.filter(talk__icontains=talk,receiver=receiver)
		return render(request,'guestbookver1.html',locals())
	if 'talk' in request.POST:
		receiver=request.POST['receiver']
		talk=request.POST['talk']
		date_time=datetime.datetime.now()
		conversation=Msg.objects.create(sender=sender, receiver=receiver,talk=talk,date_time=date_time)
		conversation=Msg.objects.filter(receiver=receiver)
	else:
		receiver=sender
	conversation=Msg.objects.filter(receiver=receiver)
	return render(request, 'guestbookver1.html',locals())

def personalpage(request):
	if request.user.is_authenticated:
		sender=request.user.username
	else:
		message="你尚未登入"
	if 'update' in request.POST:
		idex=request.POST['idex']
		receiver=request.POST['receiver']
		sender=request.POST['sender']
		newtalk=request.POST['newtalk']
		talk=request.POST['talk']
		Msg.objects.filter(id=idex,sender=sender,receiver=receiver,talk=talk).update(talk=newtalk)
	if 'delete' in request.POST:
		receiver=request.POST['receiver']
		idex=request.POST['idex']
		sender=request.POST['sender']
		talk=request.POST['talk']
		Msg.objects.filter(id=idex,receiver=receiver,sender=sender,talk=talk).delete()
	if 'search' in request.POST:
		talk=request.POST['talk']
		sender=request.POST['sender']
		conversation=Msg.objects.filter(talk__icontains=talk,sender=sender)
		return render(request,'personalpage.html',locals())
	conversation=Msg.objects.filter(sender=sender)
	return render(request,'personalpage.html',locals())



		

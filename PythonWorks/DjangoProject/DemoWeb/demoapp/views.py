from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randrange

from .models import userInfo

# Create your views here.

def index(request):
	tmp = 100
	tmp = randrange(tmp) 

	return render(request, 'demoapp/login.html')

def registerUser(request):

	return render(request, 'demoapp/register.html')
	

def default(request):
	return HttpResponse("Called default function")

def details(request):
	return render(request, 'demoapp/details.html')

# def details(request, per1):
# 	return HttpResponse("Details function called %s <a href='/'>Go Back</a>"%(per1))

def getDetails(request, per1, per2):
	return HttpResponse("Details function called perameter1 is %s and perameter2 is %s <a href='/'>Go Back</a>"%(per1, per2))

def home(request):
	allData = userInfo.objects.all()
	return render(request, 'demoapp/alluser.html', {'alluserdata': allData})


def addNewUser(request):
	if request.method == 'POST':
		name = request.POST['txtuname']
		email = request.POST['txtuemail']
		passwd = request.POST['txtupass']
		mobile = request.POST['txtumobile']

		u = userInfo(user_name=name,user_email=email,user_pass=passwd,user_mobile=mobile)
		u.save()
		msg = True		
		return redirect('home')
		# return render(request, 'alluser.html', {'msg':msg})

def removeUser(request, rid):
	if request.method == 'GET':		
		userInfo.objects.filter(id=rid).delete()
		return redirect('home')

def changeUser(request, eid):	
	eid = userInfo.objects.get(id=eid)
	print(eid.user_name)
	return render(request, 'demoapp/changeuser.html', {'editid':eid})

def edituser(request, eid):
	if request.method == 'POST':
		name = request.POST['txtuname']
		email = request.POST['txtuemail']
		passwd = request.POST['txtupass']
		mobile = request.POST['txtumobile']

		userInfo.objects.filter(id=eid).update(user_name=name,user_email=email,user_pass=passwd,user_mobile=mobile)
		return redirect('home')

def doLogin(request):
	if request.method == 'POST':		
		email = request.POST['txtuemail']
		passwd = request.POST['txtupass']

		e = userInfo.objects.get(user_email=email)
		if e.user_pass == passwd:
			request.session['name'] = e.user_name			
			return redirect('home')
		else:			
			return render(request, 'demoapp/login.html', {'errMsg':'email and password is invalid'})

def logout(request):
	del request.session['name']
	return redirect('index')
	
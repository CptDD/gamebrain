from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required



from gamestats.forms import UserForm


@login_required
def index(request):
	return render(request,'gamestats/index.html',context={})
	

def about(request):
	return render(request,'gamestats/about.html',context={})

@login_required	
def dashboard(request):
	return render(request,'gamestats/dashboard.html',context={})

@login_required
def tracker(request):
	return render(request,'gamestats/tracker.html',context={})
	
	
def register(request):
	
	registered = False
	error = False
	
	if request.method == 'POST':
		
		user_form=UserForm(data=request.POST)
		
		if user_form.is_valid():
			
			user=user_form.save()
			
			user.set_password(user.password)
			user.save()
			
			registered = True
		else:
			error = True
			print(user_form.errors)
	else:
		user_form=UserForm()
		
	return render(request,'gamestats/register.html',{'user_form':user_form,'registered':registered,'error':error})
	

def user_login(request):
		
	if request.method == 'POST':
		
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user=authenticate(username=username,password=password)
		
		if user:
			
			login(request,user)
			
			return HttpResponseRedirect(reverse('index'))
			
		else:
			return HttpResponse('Your username and password do not match!')
			
		
	else:
		return render(request,'gamestats/login.html',{})
		
@login_required
def user_logout(request):
	
	logout(request)
	return HttpResponseRedirect(reverse('index'))
	

	
	
			
	

	
	







from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm, UserProfileForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import HandyFilter
# Create your views here.




@login_required(login_url='login')
def home(request):
	profile_form = UserProfileForm()
	orders = UserProfile.objects.all()
	
	myFilter = HandyFilter(request.GET, queryset=orders)
	orders = myFilter.qs

	return render(request, 'accounts/customlanding.html', {'all':orders, 'myFilter':myFilter})

@login_required(login_url='login')
def hman(request):

	order = UserProfile.objects.get(user=request.user)
	form = UserProfileForm(instance=order)
						
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('hman')

	return render(request, 'accounts/hmanlanding.html', {'form':form})




def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			uname = request.POST.get('username')
			pword = request.POST.get('password')

			u = authenticate(request, username=uname, password=pword)
			profile_form = UserProfileForm()
			if u is not None:
				login(request, u)
					
				all_members = UserProfile.objects.all

				for item in UserProfile.objects.all():

					if (item.user.username == uname) and (item.typeOfProfile == 'Customer'):
						
						
						
								
											



						return redirect('home')
					else:
						
						return redirect('hman')
					
			else:
				messages.info(request, 'Username or password is incorrect.')


	context = {}
	return render(request, 'accounts/login.html', context)



def logoutPage(request):
	logout(request)
	return redirect('login')

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm();

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			profile_form = ProfileForm(request.POST)
			if form.is_valid() and profile_form.is_valid():

				user = form.save()
				profile = profile_form.save(commit=False)
				profile.user = user
				profile.save()

				uname = form.cleaned_data.get('username')
				messages.success(request, 'Account successfully created for ' + uname)
				return redirect('login')
			novalidate = True
		else:
			form = CreateUserForm()
			profile_form = ProfileForm()


	context = {'form':form, 'profile_form':profile_form}
	return render(request, 'accounts/register.html', context)

def CreateUpdateForm(request):
	form = UpdateForm()
	if request.method == 'POST':
		form = UpdateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')



def payment(request):
    return render(request, 'payments/index.html')
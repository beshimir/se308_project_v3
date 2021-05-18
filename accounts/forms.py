





from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile






class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2',]



class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = '__all__'
		exclude = ['typeOfProfile', 'user',]

class ProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['typeOfProfile']


class DoubleForm(CreateUserForm, UserProfileForm):
	class Meta:
		model = UserProfile
		fields = '__all__'
		exclude = ['user', 'typeOfProfile']

from django.db import models


from django.contrib.auth.models import User





# Create your models here.


class UserProfile(models.Model):
	
	

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	PROFILES = (	('Customer', 'Customer'),
				('Handyman', 'Handyman'))

	JOBS = (	('Plumber', 'Plumber'),
				('Carpenter', 'Carpenter'),
				('Electrician', 'Electrician'),
				('Testwork', 'Testwork')
		)

	typeOfProfile = models.CharField(max_length=100, choices=PROFILES)
	typeOfJob = models.CharField(max_length=100, choices=JOBS, default="not found...", blank=True)
	description = models.TextField(default='not found...', blank=True)
	location = models.CharField(max_length=50, default='not found...', blank=True)
	experience = models.IntegerField(default=0, blank=True)
	avatar = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.user.username
		return self.user.typeOfProfile

import django_filters

from .models import *

class HandyFilter(django_filters.FilterSet):
	class Meta:
		model = UserProfile
		fields = ['typeOfJob', 'location', 'experience',]
from django.urls import path
from . import views
from handymanapp import settings
from django.conf.urls.static import static
from django.conf.urls import include


urlpatterns = [

	path('customlanding/', views.home, name="home"),
	path('login/', views.loginPage, name="login"),
	path('register/', views.register, name="register"),
	path('logout/', views.logoutPage, name="logout"),

	
	path('hmanlanding/', views.hman, name="hman"),
	path('payment/', include('payments.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
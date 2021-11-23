from django.conf.urls import url
from gamestats import views

urlpatterns=[
	url(r'^$',views.index,name='index'),
	url(r'^about$',views.about,name='about'),
	url(r'^dashboard$',views.dashboard,name='dashboard'),
	url(r'^tracker$',views.tracker,name='tracker'),
	url(r'^login$',views.user_login,name='login'),
	url(r'^logout$',views.user_logout,name='logout'),
	url(r'^register$',views.register,name='register'),
	
]

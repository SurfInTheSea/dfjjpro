from django.urls import path
from django.urls import re_path
from . import views



urlpatterns = [
	path('', views.index,name='index'),
	path('index/', views.index, name='index'),
	path('newguide/', views.newguide, name='newguide'),
	path('maintz/', views.maintz, name='maintz'),
	path('userCenter/', views.userCenter, name='userCenter'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('register/', views.register, name='register'),
	path('banckAndaccount/', views.banckAndaccount, name='banckAndaccount'),
	path('personalProgramDetails/', views.personalProgramDetails, name='personalProgramDetails'),
	# path('programDetails/(?P<pk>[0-9]+)/$', indexView.programDetails, name='programDetails'),
	# r'^comments/(?:page-(?P<page_number>\d+)/)?$'
	# path(r'^programDetails/(?:page-(?P<page_number>\d+)/)?$', indexView.programDetails, name='programDetails'),
	re_path('programDetails/(?P<pk>[0-9]+)/$', views.programDetails, name='programDetails'),
	re_path('programDetails/(?P<pk>[0-9]+)/buyProgramDetails/$', views.buyProgramDetails, name='buyProgramDetails'),

]
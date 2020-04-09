from django.urls import path
from . import views

app_name = 'myChatbot'

urlpatterns = [
	#path('', views.CommandCreate.as_view(), name='mychatbot_list')
	path('', views.command_create, name='command_create')
]

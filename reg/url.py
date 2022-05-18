from django.urls import path
from . import views
urlpatterns=[
    path('', views.login, name='home'),
    path('newu', views.newu, name='newu')

]
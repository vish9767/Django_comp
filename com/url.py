from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home,name='home'),
    path('com',views.comp,name="com"),
    path('hom',views.hom,name="hom"),
    path('mob',views.mob,name="mob")
]

from django.conf.urls import url
from django.urls import path, include
from . import views


app_name = 'courseSelection'
urlpatterns = [
                path('stuSelect',views.stuSelect,name="stuSelect"),
                  path('', views.welcome, name="welcome"),
              ]

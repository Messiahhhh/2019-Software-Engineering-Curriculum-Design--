from django.conf.urls import url
from django.urls import path, include
from . import views


app_name = 'graduationManagement'
urlpatterns = [
                  path('', views.welcome, name="welcome"),
<<<<<<< HEAD
=======
                  path('func', views.func, name="func"),
>>>>>>> b12887070dca45507f23fcc57d4d880354fe094e
              ]

from django.conf.urls import url
from . import views
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'courseSelection'
urlpatterns = [
                  path('', views.welcome, name="welcome"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

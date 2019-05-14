from django.conf.urls import url
from django.contrib import admin
#from django.urls import path

from . import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='not-sorted'),
    url(r'^stars/', views.stars, name='sorted-by-stars'),
    url(r'^updated/', views.updated, name='sorted-by-updated'),
]

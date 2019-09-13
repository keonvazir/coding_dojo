########## APP LEVEL urls.py #############

from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money$', views.process_money),
    url(r'^clear$', views.clear),
]
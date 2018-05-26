from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^event_detail/(\d+)', event_detail, name="event_detail"),
    
]
from django.conf.urls import url
from .views import information

urlpatterns = [
    url(r'info/(?P<id>\d+)/$', information, name="reservation_info"),
]
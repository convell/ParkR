from django.conf.urls import url
from .views import information, new_reservation, reservation_history, process

urlpatterns = [
    url(r'info/(?P<id>\d+)/$', information, name="reservation_info"),
    url(r'reservation/(?P<id>\d+)/$', new_reservation, name="new_reservation"),
    url(r'history$', reservation_history, name="reservation_history"),
    url(r'process$', process, name='process'),
]
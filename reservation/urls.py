from django.conf.urls import url
from .views import information, reservation_history, reservation_receipt, process, delete_reservation

urlpatterns = [
    url(r'info/(?P<id>\d+)/$', information, name="reservation_info"),
    url(r'history$', reservation_history, name="reservation_history"),
    url(r'history/deleted_reservation/(?P<id>\d+)/$', delete_reservation, name="delete_reservation"),
    url(r'receipt$', reservation_receipt, name="reservation_receipt"),
    url(r'process$', process, name='process'),
]
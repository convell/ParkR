
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^payment/$', views.payment, name='payment'),
    url(r'^process/$', views.process, name='process'),
]

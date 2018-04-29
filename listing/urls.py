from django.conf.urls import url
from .views import new_space, delete_space


urlpatterns = [
    url(r'new_space', new_space, name="new_space"),
    url(r'profile/deleted_space/(?P<id>\d+)/$', delete_space, name="delete_space"),
]
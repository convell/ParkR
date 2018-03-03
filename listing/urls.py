from django.conf.urls import url
from .views import new_space


urlpatterns = [
    url(r'new_space', new_space, name="new_space"),
]
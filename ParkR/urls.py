"""ParkR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_private_chat import urls as django_private_chat_urls

from .views import home, privacy

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="parkr_home"),
    url(r'^account/', include('account.urls')),
    url(r'^list/', include('listing.urls')),
    url(r'^reserve/', include('reservation.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^', include('django_private_chat.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^privacy/', privacy, name="parkr_privacy"),
]
urlpatterns += staticfiles_urlpatterns()

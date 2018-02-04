"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from parkr import views
urlpatterns = [
    url(r'^login/$', auth_views.login,{'template_name':'login.html'},name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/'},name='logout'),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^reserve/$', views.reserve, name='reserve'),
    url(r'^signup/$', views.signup, name='register'),
    url(r'^test/$', views.test, name='test'),
    url(r'^passwordChange/$', views.passwordChange, name='password'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate')
]
urlpatterns += staticfiles_urlpatterns()

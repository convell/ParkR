from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .views import SignUpView, profile, show


urlpatterns = [
    url(r'login$',
        LoginView.as_view(template_name="account/login_form.html"),
        name="user_login"),
    url(r'logout$',
        LogoutView.as_view(),
        name="user_logout"),
    url(r'signup$',
        SignUpView.as_view(),
        name='user_signup'),
    url(r'profile$', profile, name="user_profile"),
    url(r'show/(?P<id>\d+)/$', show, name="user_show"),
    url(r'change-password/',
        PasswordChangeView.as_view(template_name="account/change_password.html"),
        name="user_password"),
]
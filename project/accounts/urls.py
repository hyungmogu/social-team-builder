from django.conf.urls import url

from . import views

# API endpoints
urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^logout/$', views.LogOutView.as_view(), name="logout"),
    url(r'^sign_up/$', views.SignUpView.as_view(), name="sign_up"),
]

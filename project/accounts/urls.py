from django.conf.urls import url

import main.views as views

# API endpoints
urlpatterns = [
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^sign_up/$', views.signup, name="sign_up"),
]

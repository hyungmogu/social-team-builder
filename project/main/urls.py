from django.conf.urls import url

import main.views as views

# API endpoints
urlpatterns = [
    url(r'^$', views.home, name="home"),
]

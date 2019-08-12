from django.conf.urls import url

import main.views as views

# API endpoints
urlpatterns = [
    url(r'^projects/(?P<project_pk>\d+)/edit/$', views.project_edit, name="project_edit"),
    url(r'^projects/(?P<project_pk>\d+)/$', views.project, name="project"),
    url(r'^profiles/(?P<user_pk>\d+)/edit/$', views.profile_edit, name="profile_edit"),
    url(r'^profiles/(?P<user_pk>\d+)/$', views.profile, name="profile"),
    url(r'^projects/create/$', views.project_create, name="project_create"),
    url(r'^search/$', views.search, name="search"),
    url(r'^applications/$', views.applications, name="application"),
    url(r'^$', views.home, name="home"),
]

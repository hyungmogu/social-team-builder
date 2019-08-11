from django.conf.urls import url

import main.views as views

# API endpoints
urlpatterns = [
    url(r'^profile/(?P<user_pk>\d+)/$', views.profile, name="profile"),
    url(r'^profile/(?P<user_pk>\d+)/edit/$', views.profile_edit, name="profile-edit"),
    url(r'^project/(?P<project_pk>\d+)/$', views.project, name="project"),
    url(r'^project/(?P<project_pk>\d+)/edit/$', views.project_edit, name="project-edit"),
    url(r'^project/(?P<project_pk>\d+)/create/$', views.project_create, name="project-create"),
    url(r'^search/$', views.search, name="search"),
    url(r'^applications/$', views.applications, name="application"),
    url(r'^$', views.home, name="home"),
]

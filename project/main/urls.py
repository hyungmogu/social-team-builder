from django.conf.urls import url

import main.views as views

# API endpoints
urlpatterns = [
    url(r'^projects/(?P<pk>\d+)/delete/$', views.ProjectDeleteView.as_view(), name="project_delete"),
    url(r'^projects/(?P<pk>\d+)/edit/$', views.ProjectEditView.as_view(), name="project_edit"),
    url(r'^projects/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name="project"),
    url(r'^projects/create/$', views.ProjectCreateView.as_view(), name="project_create"),
    url(r'^profile/(?P<pk>\d+)/edit/$', views.ProfileEditView.as_view(), name="profile_edit"),
    url(r'^profile/(?P<pk>\d+)/$', views.ProfileView.as_view() , name="profile"),
    url(r'^search/by_position/$', views.SearchByPositionView.as_view(), name="search_position"),
    url(r'^search/$', views.SearchView.as_view(), name="search"),
    url(r'^applications/(?P<pk>\d+)/$', views.applications, name="application"),
    url(r'^$', views.HomeView.as_view(), name="home"),
]

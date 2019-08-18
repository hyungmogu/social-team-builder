from django.conf.urls import url

import main.views as views

# API endpoints
urlpatterns = [
    url(r'^projects/(?P<project_pk>\d+)/positions/(?P<position_pk>\d+)/apply/$', views.ApplicationSubmitView.as_view(), name="apply"),
    url(r'^projects/(?P<pk>\d+)/delete/$', views.ProjectDeleteView.as_view(), name="project_delete"),
    url(r'^projects/(?P<pk>\d+)/edit/$', views.ProjectEditView.as_view(), name="project_edit"),
    url(r'^projects/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name="project"),
    url(r'^projects/create/$', views.ProjectCreateView.as_view(), name="project_create"),
    url(r'^profile/(?P<pk>\d+)/edit/$', views.ProfileEditView.as_view(), name="profile_edit"),
    url(r'^profile/(?P<pk>\d+)/$', views.ProfileView.as_view() , name="profile"),
    url(r'^search/by_position/$', views.SearchByPositionView.as_view(), name="search_position"),
    url(r'^search/$', views.SearchView.as_view(), name="search"),
    url(r'^applications/applicants/(?P<pk>\d+)/edit/$', views.ApplicantEditView.as_view(), name="applicant_edit"),
    url(r'^applications/by_proj_need/$', views.ApplicationsByProjectNeedView.as_view(), name="applications_proj_need"),
    url(r'^applications/by_project/$', views.ApplicationsByProjectView.as_view(), name="applications_project"),
    url(r'^applications/by_status/$', views.ApplicationsByStatusView.as_view(), name="applications_status"),
    url(r'^applications/$', views.ApplicationsView.as_view(), name="applications"),
    url(r'^$', views.HomeView.as_view(), name="home"),
]

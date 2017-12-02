from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreatePatrolView, CreateParticipantView, PatrolDetailView, ParticipantDetailView
from .views import CreatePatrolAdminView, CreateParticipantAdminView
from .views import PatrolDetailAdminView, ParticipantDetailAdminView

urlpatterns = {
    url(r'^patrol/$', CreatePatrolView.as_view(), name="create_patrol"),
    url(r'^participant/$', CreateParticipantView.as_view(), name="create_participant"),
    url(r'^admin/patrol/$', CreatePatrolAdminView.as_view(), name="create_patrol"),
    url(r'^admin/participant/$', CreateParticipantAdminView.as_view(), name="create_participant"),

    url(r'^patrol/(?P<pk>\d+)$', PatrolDetailView.as_view(), name="edit_patrol"),
    url(r'^participant/(?P<pk>\d+)$', ParticipantDetailView.as_view(), name="edit_participant"),
    url(r'^admin/patrol/(?P<pk>\d+)$', PatrolDetailAdminView.as_view(), name="edit_patrol"),
    url(r'^admin/participant/(?P<pk>\d+)$', ParticipantDetailAdminView.as_view(), name="edit_participant"),
}

urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreatePatrolView, CreateParticipantView, PatrolDetailView, ParticipantDetailView

urlpatterns = {
    url(r'^patrol/$', CreatePatrolView.as_view(), name="create_patrol"),
    url(r'^participant/$', CreateParticipantView.as_view(), name="create_participant"),
    url(r'^patrol/(?P<pk>\d+)$', PatrolDetailView.as_view(), name="edit_patrol"),
    url(r'^participant/(?P<pk>\d+)$', ParticipantDetailView.as_view(), name="edit_participant"),
}

urlpatterns = format_suffix_patterns(urlpatterns)

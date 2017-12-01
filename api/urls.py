from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreatePatrolView, CreateParticipantView

urlpatterns = {
    url(r'^patrol/$', CreatePatrolView.as_view(), name="create_patrol"),
    url(r'^participant/$', CreateParticipantView.as_view(), name="create_participant"),
}

urlpatterns = format_suffix_patterns(urlpatterns)

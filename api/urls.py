from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views
from .views import CreatePatrolView, CreateParticipantView, PatrolDetailView, ParticipantDetailView
from .views import CreatePatrolAdminView, CreateParticipantAdminView
from .views import PatrolDetailAdminView, ParticipantDetailAdminView
from .views import CreateMailboxView, CreateMessageView
from .views import DeleteMailboxView, DeleteMessageView

urlpatterns = {
	# CREATE
    url(r'^patrol/$', CreatePatrolView.as_view(), name="create_patrol"),
    url(r'^participant/$', CreateParticipantView.as_view(), name="create_participant"),
    url(r'^admin/patrol/$', CreatePatrolAdminView.as_view(), name="create_patrol"),
    url(r'^admin/participant/$', CreateParticipantAdminView.as_view(), name="create_participant"),
    url(r'^admin/mailbox/$', CreateMailboxView.as_view(), name="create_mailbox"),
    url(r'^admin/message/$', CreateMessageView.as_view(), name="create_message"),

    # EDIT
    url(r'^patrol/(?P<pk>\d+)$', PatrolDetailView.as_view(), name="edit_patrol"),
    url(r'^participant/(?P<pk>\d+)$', ParticipantDetailView.as_view(), name="edit_participant"),
    url(r'^admin/patrol/(?P<pk>\d+)$', PatrolDetailAdminView.as_view(), name="edit_patrol"),
    url(r'^admin/participant/(?P<pk>\d+)$', ParticipantDetailAdminView.as_view(), name="edit_participant"),

    # DELETE
    url(r'^admin/mailbox/(?P<pk>\d+)$', DeleteMailboxView.as_view(), name="delete_mailbox"),
    url(r'^admin/message/(?P<pk>\d+)$', DeleteMessageView.as_view(), name="delete_message"),

    url(r'^token/', views.obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)

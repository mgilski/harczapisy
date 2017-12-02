from rest_framework import generics
from .serializers import PatrolListSerializer, ParticipantListSerializer
from .serializers import PatrolListAdminSerializer, ParticipantListAdminSerializer
from .serializers import MailboxSerializer, MessageListSerializer
from .models import PatrolList, ParticipantList, MailboxList, MessageList


##### PATROL

class CreatePatrolView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = PatrolList.objects.all()
    serializer_class = PatrolListSerializer


class CreatePatrolAdminView(CreatePatrolView):
    serializer_class = PatrolListAdminSerializer


class PatrolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatrolList.objects.all()
    serializer_class = PatrolListSerializer


class PatrolDetailAdminView(PatrolDetailView):
    serializer_class = PatrolListAdminSerializer



##### PARTICIPANT

class CreateParticipantView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ParticipantList.objects.all()
    serializer_class = ParticipantListSerializer


class CreateParticipantAdminView(CreateParticipantView):
    serializer_class = ParticipantListAdminSerializer


class ParticipantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParticipantList.objects.all()
    serializer_class = ParticipantListSerializer


class ParticipantDetailAdminView(ParticipantDetailView):
    serializer_class = ParticipantListAdminSerializer


##### MAILBOX

class CreateMailboxView(generics.ListCreateAPIView):
    queryset = MailboxList.objects.all()
    serializer_class = MailboxSerializer


class DeleteMailboxView(generics.RetrieveDestroyAPIView):
    queryset = MailboxList.objects.all()
    serializer_class = MailboxSerializer


class CreateMessageView(generics.ListCreateAPIView):
    queryset = MessageList.objects.all()
    serializer_class = MessageListSerializer


class DeleteMessageView(generics.RetrieveDestroyAPIView):
    queryset = MessageList.objects.all()
    serializer_class = MessageListSerializer
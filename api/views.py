from rest_framework import generics
from .serializers import PatrolListSerializer, ParticipantListSerializer
from .serializers import PatrolListAdminSerializer, ParticipantListAdminSerializer
from .serializers import MailboxSerializer, MessageListSerializer
from .models import PatrolList, ParticipantList, MailboxList, MessageList
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


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

    def perform_create(self, serializer):
        serializer.save()
        if serializer.data['leader'] == True:
            user = User.objects.create_user(username=serializer.data['pesel'],
                                            email=serializer.data['leader_email'],
                                            password='wH%^jy`EW)&#AN9Y')
            token = str(Token.objects.get_or_create(user=user)[0])


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
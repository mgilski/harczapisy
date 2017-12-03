from rest_framework import generics
from .serializers import PatrolListSerializer, ParticipantListSerializer
from .serializers import PatrolListAdminSerializer, ParticipantListAdminSerializer
from .serializers import PatrolListUserSerializer, ParticipantListUserSerializer
from .serializers import MailboxSerializer, MessageListSerializer
from .models import PatrolList, ParticipantList, MailboxList, MessageList
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail


##### PATROL

## Create
class ParentCreatePatrolView(generics.ListCreateAPIView):
    queryset = PatrolList.objects.all()


class CreatePatrolUserView(ParentCreatePatrolView):
    """This class defines the create behavior of our rest api."""
    serializer_class = PatrolListUserSerializer


class CreatePatrolAdminView(ParentCreatePatrolView):
    serializer_class = PatrolListAdminSerializer


class CreatePatrolView(ParentCreatePatrolView):
    serializer_class = PatrolListSerializer




## Detail
class ParentPatrolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatrolList.objects.all()


class PatrolDetailUserView(ParentPatrolDetailView):
    serializer_class = PatrolListUserSerializer


class PatrolDetailAdminView(ParentPatrolDetailView):
    serializer_class = PatrolListAdminSerializer


class PatrolDetailView(ParentPatrolDetailView):
    serializer_class = PatrolListSerializer



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
            send_mail(
                'test',
                f'token: {token}',
                '',
                [serializer.data['leader_email']],
                fail_silently=False,
            )



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
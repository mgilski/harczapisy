from rest_framework import generics
from .serializers import PatrolListSerializer, ParticipantListSerializer
from .serializers import PatrolListAdminSerializer, ParticipantListAdminSerializer
from .models import PatrolList, ParticipantList

class CreatePatrolView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = PatrolList.objects.all()
    serializer_class = PatrolListSerializer


class CreatePatrolAdminView(CreatePatrolView):
    serializer_class = PatrolListAdminSerializer


class CreateParticipantView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ParticipantList.objects.all()
    serializer_class = ParticipantListSerializer


class CreateParticipantAdminView(CreateParticipantView):
    serializer_class = ParticipantListAdminSerializer


class PatrolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatrolList.objects.all()
    serializer_class = PatrolListSerializer


class PatrolDetailAdminView(PatrolDetailView):
    serializer_class = PatrolListAdminSerializer


class ParticipantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParticipantList.objects.all()
    serializer_class = ParticipantListSerializer


class ParticipantDetailAdminView(ParticipantDetailView):
    serializer_class = ParticipantListAdminSerializer
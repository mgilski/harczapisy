from rest_framework import generics
from .serializers import PatrolListSerializer, ParticipantListSerializer
from .models import PatrolList, ParticipantList

class CreatePatrolView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = PatrolList.objects.all()
    serializer_class = PatrolListSerializer


class CreateParticipantView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ParticipantList.objects.all()
    serializer_class = ParticipantListSerializer


class PatrolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatrolList.objects.all()
    serializer_class = PatrolListSerializer


class ParticipantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParticipantList.objects.all()
    serializer_class = ParticipantListSerializer
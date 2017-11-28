from rest_framework import generics
from .serializers import PatrolListSerializer, ParticipantListSerializer
from .models import PatrolList, ParticipantList

class CreatePatrolView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = PatrolList.objects.all()
    serializer_class = PatrolListSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class CreateParticipantView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ParticipantList.objects.all()
    serializer_class = ParticipantListSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
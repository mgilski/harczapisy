from rest_framework import generics
from .serializers import PatrolListSerializer
from .models import PatrolList

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = PatrolList.objects.all()
    serializer_class = PatrolListSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
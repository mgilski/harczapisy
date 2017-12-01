import json
from django.test import TestCase
from .models import PatrolList, ParticipantList
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

participant_row = json.loads('''
    {
        "patrol": 0,
        "pesel": "97090515811",
        "first_name": "Jan",
        "second_name": "Dom",
        "last_name": "Kowalski",
        "instructor_rank": "pwd",
        "which_service": 4,
        "service_type": "med",
        "rescue_course": "wkpp",
        "which_rescue_service": 2,
        "rescue_certificate": "http://test.com/certificates/cert.pdf",
        "leader": true,
        "leader_email": "janek@gmail.com"
    }
''')

patrol_row = json.loads('''
    {
        "name": "Super patrol",
        "hufiec": "Siedem"
    }
''')

class ModelTestCase(TestCase):
    """Test suite for PatrolList and ParticipantList models"""

    def setUp(self):
        """Define the test client and other test variables."""

        patrol_data = dict(patrol_row)
        self.patrollist = PatrolList(**patrol_data)
        patrol_data['name'] = 'Super patrol 2'
        PatrolList.objects.create(**patrol_data)
        print(PatrolList.objects.values('id'))
        participant_data = dict(participant_row)
        participant_data['patrol'] = PatrolList.objects.latest('id')
        self.participantlist = ParticipantList(**participant_data)

    def test_model_can_create_a_patrollist(self):
        """Test the PatrolList model can create a PatrolList."""
        old_count = PatrolList.objects.count()
        self.patrollist.save()
        new_count = PatrolList.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_a_participantlist(self):
        """Test the ParticipantList model can create a ParticipantList."""
        old_count = ParticipantList.objects.count()
        self.participantlist.save()
        new_count = ParticipantList.objects.count()
        self.assertNotEqual(old_count, new_count)



class CreateParticipantTestCase(TestCase):
    """Test suite for creating participant."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.participant_data = dict(participant_row)
        self.patrol_data = dict(patrol_row)
        PatrolList.objects.create(**patrol_row)
        self.participant_data['patrol'] = PatrolList.objects.latest('id').id
        
        
    def test_creating_participant(self):
        """Test the api has participant creation capability."""
        print(reverse('create_participant'))
        self.response = self.client.post(
            reverse('create_participant'),
            self.participant_data,
            format="json")

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

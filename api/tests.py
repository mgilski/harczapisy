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

        patrol_data1 = dict(patrol_row)
        patrol_data2 = dict(patrol_row)
        self.patrollist = PatrolList(**patrol_data1)
        patrol_data2['name'] = 'Super patrol 2'
        PatrolList.objects.create(**patrol_data2)
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

    def create_participant_test(self, succeed, key=None, value=None):
        participant_data = dict(self.participant_data)
        if key is not None:
            participant_data[key] = value
        self.response = self.client.post(
            reverse('create_participant'),
            participant_data,
            format="json")
        if succeed:
            code = status.HTTP_201_CREATED
        else:
            code = status.HTTP_400_BAD_REQUEST
        self.assertEqual(self.response.status_code, code)

    def test_creating_participant(self):
        """Test if the api has participant creation capability."""
        self.create_participant_test(True)

    def test_creating_participant_wrong_pesel(self):
        """Test if the api has participant creation capability with wrong PESEL"""
        self.create_participant_test(False, 'pesel', '97090515810')
        self.create_participant_test(False, 'pesel', '12312312312')
        self.create_participant_test(False, 'pesel', '12312312312')
        self.create_participant_test(False, 'pesel', '85743839548')
        self.create_participant_test(False, 'pesel', '63526748492')
        self.create_participant_test(False, 'pesel', '')

    def test_creating_participant_wrong_rank(self):
        """Test if the api has participant creation capability with wrong instructor rank"""
        self.create_participant_test(False, 'instructor_rank', 'pwd.')
        self.create_participant_test(False, 'instructor_rank', 'phm.')
        self.create_participant_test(False, 'instructor_rank', 'hm.')
        self.create_participant_test(False, 'instructor_rank', 'pw')
        self.create_participant_test(False, 'instructor_rank', 'ph')
        self.create_participant_test(False, 'instructor_rank', '')

    def test_creating_participant_wrong_email(self):
        """Test if the api has participant creation capability with wrong email"""
        self.create_participant_test(False, 'leader_email', 'leon@gmail')
        self.create_participant_test(False, 'leader_email', 'leon@gmail.')
        self.create_participant_test(False, 'leader_email', '@gmail')
        self.create_participant_test(False, 'leader_email', '@gmail.com')
        self.create_participant_test(False, 'leader_email', 'leon@')
        self.create_participant_test(False, 'leader_email', '')

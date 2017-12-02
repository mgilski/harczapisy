from rest_framework import serializers
from .models import PatrolList, ParticipantList
from rest_framework.serializers import ValidationError

# TODO: rescue service number validator, one leader validator, one pesel validator



class PatrolListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = PatrolList
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')
        # validators = [
        #     UniqueValidator(queryset=PatrolList.objects.values('name')),

        # ]


class ParticipantListSerializer(serializers.ModelSerializer):
    """Participant serializer."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ParticipantList
        fields = ('patrol','pesel','first_name',
                  'second_name','last_name','instructor_rank',
                  'which_service','service_type','rescue_course',
                  'which_rescue_service','rescue_certificate',
                  'leader','leader_email','date_created','date_modified')
        read_only_fields = ('date_created', 'date_modified')

    def validate_pesel(self, pesel_str):
        pesel = [ int(pesel_digit) for pesel_digit in pesel_str ]
        validation_number = 9*pesel[0] + 7*pesel[1] + 3*pesel[2] + \
                            1*pesel[3] + 9*pesel[4] + 7*pesel[5] + \
                            3*pesel[6] + 1*pesel[7] + 9*pesel[8] + \
                            7*pesel[9]
        validation_digit = validation_number % 10
        if pesel[10] != validation_digit:
            raise ValidationError('Wrong PESEL.')
        return pesel_str

    def validate(self, data):
        def check_requirement(req, field):
            """field can only be filled under req condition"""
            if req and not data[field]:
                raise ValidationError(f'{field} cannot be blank')
            if not req and data[field]:
                raise ValidationError(f'{field} must be blank')

        check_requirement(data['leader'], 'leader_email')
        check_requirement(data['service_type'] == 'med', 'rescue_course')
        check_requirement(data['service_type'] == 'med', 'rescue_certificate')
        check_requirement(data['service_type'] == 'med', 'which_rescue_service')

        if ParticipantList.objects.filter(patrol=data['patrol']).filter(leader=True).count() > 0 \
        	and data['leader'] == True:
        	raise ValidationError("Patrol can't have two leaders.")
        return data

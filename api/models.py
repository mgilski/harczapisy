from django.db import models

class PatrolList(models.Model):
    """Klasa reprezentująca model patrolu."""
    name = models.CharField(max_length=255, unique=True)
    hufiec = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return f'{self.name}, {self.hufiec}'


class ParticipantList(models.Model):
    """Klasa reprezentująca model uczestnika."""
    RANKS = (
        ('pwd', 'pwd.'),
        ('phm', 'phm.'),
        ('hm', 'hm.'),
    )
    SERVICES = (
        ('lit', 'Liturgiczno-reprezentacyjna'),
        ('med', 'Medyczna'),
        ('wew', 'Wewnętrzna'),
        ('szt', 'Sztab'),
        ('tv', 'Medialna'),
        ('cln', 'Porządkowa'),
    )
    patrol = models.ForeignKey(PatrolList, on_delete=models.CASCADE)
    pesel = models.CharField(max_length=11, unique=True)
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40)
    instructor_rank = models.CharField(max_length=3, choices=RANKS, blank=True)
    which_service = models.IntegerField()
    service_type = models.CharField(max_length=3, choices=SERVICES)
    rescue_course = models.CharField(max_length=255, blank=True)
    which_rescue_service = models.IntegerField(null=True)
    rescue_certificate = models.URLField(blank=True)
    leader = models.BooleanField()
    leader_email = models.EmailField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return f'{first_name} {last_name}'

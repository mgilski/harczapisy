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
    bus = models.BooleanField(default=False)
    cash = models.BooleanField(default=False)
    rescue_course = models.CharField(max_length=255, blank=True)
    which_rescue_service = models.IntegerField(null=True)
    rescue_certificate = models.URLField(blank=True)
    leader = models.BooleanField(default=False)
    leader_email = models.EmailField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return f'{self.first_name} {self.last_name}'


class MailboxList(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.email)


class MessageList(models.Model):
    DIRECTION = (('in', 'in'), ('out', 'out'))
    mailbox = models.ForeignKey(MailboxList, on_delete=models.CASCADE)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    direction = models.CharField(max_length=3, choices=DIRECTION)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email}, {self.direction}: {self.subject}'
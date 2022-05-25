from django.db import models


# Create your models here.
class Incident(models.Model):
    location = models.CharField(max_length=22)
    incident_department = models.TextField()
    date = models.DateField()
    incident_location = models.TextField()
    initial_severity = models.TextField()
    suspected_cause = models.TextField()
    immediate_action_taken = models.TextField()
    sub_incident_type = models.TextField()


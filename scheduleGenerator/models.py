from django.db import models

# Create your models here.
class reservedTime (models.Model):
    # Using Django Default to provide ID key
    description = models.CharField(max_length=250, blank=True)
    startTime = models.TimeField(auto_now=False, auto_now_add=False)
    endTime = models.TimeField(auto_now=False, auto_now_add=False)
    sectionID = models.IntegerField(primary_key=True, default=0)
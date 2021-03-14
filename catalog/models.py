from django.db import models

# Create your models here.
class course (models.Model):
    departmentID = models.IntegerField
    courseNumber = models.IntegerField
    courseTitle = models.CharField(max_length=None)

class section (models.Model):
    departmentID = models.IntegerField
    courseNumber = models.IntegerField

class reservedTime (models.Model):
    description = models.CharField(max_length=250)
    startTime = models.TimeField(auto_now=False, auto_now_add=False)
    endTime = models.TimeField(auto_now=False, auto_now_add=False)
    sectionID = models.IntegerField
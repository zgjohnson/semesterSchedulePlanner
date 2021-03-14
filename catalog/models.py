from django.db import models

# Create your models here.
class course (models.Model):
    departmentID = models.IntegerField
    courseNumber = models.IntegerField(primary_key=True)
    courseTitle = models.CharField(max_length=100, default="x")

class section (models.Model):
    sectionID = models.IntegerField(primary_key=True)
    courseNumber = models.IntegerField

class reservedTime (models.Model):
    description = models.CharField(max_length=250, default="x")
    startTime = models.TimeField(auto_now=False, auto_now_add=False)
    endTime = models.TimeField(auto_now=False, auto_now_add=False)
    sectionID = models.IntegerField(primary_key=True)
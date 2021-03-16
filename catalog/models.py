from django.db import models


# Create your models here.
class course(models.Model):

    departmentID = models.IntegerField("Department ID")
   # courseNumber = models.IntegerField(primary_key=True, default=0, "Course Number")
    courseTitle = models.CharField(max_length=250, blank=True, "Course Title")


class section(models.Model):
    # Using Django Default to provide ID key
    # sectionID = models.IntegerField(primary_key=True, default=0, "Section ID", )
    courseNumber = models.IntegerField("Course Number")


class classPeriod(models.Model):
    #Using Django Default to provide ID key
    meetingDays = models.CharField(max_length=50, blank=True, "Meeting Days")
    time = models.TimeField("Time")



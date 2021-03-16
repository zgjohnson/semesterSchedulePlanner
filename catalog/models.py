from django.db import models


# Create your models here.
class course(models.Model):

    department_ID = models.IntegerField(default=None)
   # courseNumber = models.IntegerField(primary_key=True, default=0, "Course Number")
    course_title = models.CharField(max_length=250, blank=True)


class section(models.Model):
    # Using Django Default to provide ID key
    # sectionID = models.IntegerField(primary_key=True, default=0, "Section ID", )
    course_number = models.IntegerField(blank=True)


class classPeriod(models.Model):
    #Using Django Default to provide ID key
    meeting_days = models.CharField(max_length=50, blank=True)
    time = models.TimeField(blank=True)



from django.db import models


# Create your models here.
class course(models.Model):

    department_ID = models.CharField(max_length=4, primary_key=True, default="")
    courseNumber = models.IntegerField(default=0)
    course_title = models.CharField(max_length=250, default="")


class section(models.Model):
    #Using Django Default to provide ID key
    sectionID = models.IntegerField(primary_key=True, default=0 )
    course_number = models.IntegerField(blank=True, default=0)


class classPeriod(models.Model):
    #Using Django Default to provide ID key
    meeting_days = models.CharField(max_length=50, blank=True)
    time = models.TimeField(blank=True)



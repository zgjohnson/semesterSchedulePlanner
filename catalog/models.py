from django.db import models


# Create your models here.
class course(models.Model):
    departmentID = models.IntegerField
    courseNumber = models.IntegerField(primary_key=True, default=0)
    courseTitle = models.CharField(max_length=None, blank=True)


class section(models.Model):
    sectionID = models.IntegerField(primary_key=True, default=0)
    courseNumber = models.IntegerField


#class classPeriod(models.Model):
 #   class Meta:
  #      unique_together = (('meetingDays', 'time'),)

   #     meetingDays = models.CharField()
    #    time = models.TimeField()
# used a solution from StackOverflow to make a composite key
# https://stackoverflow.com/questions/28712848/composite-primary-key-in-django

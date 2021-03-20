from django.db import models


# Create your models here.
class Course(models.Model):
    departmentID = models.CharField("department ID", max_length=4)
    courseNumber = models.CharField("course Number", max_length=4)
    courseTitle = models.CharField("course Title", max_length=25, default='')

    def __str__(self):
        return self.courseTitle


class Period(models.Model):
    startTime = models.TimeField()
    endTime = models.TimeField()
    DAY_CHOICES = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('R', 'Thursday'),
        ('F', 'Friday'),
        ('MW', 'Monday, Wednesday'),
        ('MWF', 'Monday, Wednesday, Friday'),
        ('TR', 'Tuesday, Thursday'),
        ('MTWRF', 'Monday, Tuesday, Wednesday, Thursday, Friday')
    )
    meetingDays = models.CharField(max_length=5, choices=DAY_CHOICES)

    def __str__(self):
        return str(self.meetingDays) + " " + str(self.startTime) + "-" + str(self.endTime)


class Section(models.Model):
    sectionID = models.CharField("section ID", max_length=4)
    instructor = models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    periods = models.ManyToManyField(Period)

    def __str__(self):
        return self.sectionID






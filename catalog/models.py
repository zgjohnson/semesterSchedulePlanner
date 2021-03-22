from django.db import models


# Create your models here.
class Course(models.Model):
    #Using Course Number as primary key
    departmentID = models.CharField("Department ID", max_length=4)
    courseNumber = models.CharField("Course Number", max_length=4, primary_key=True)
    courseTitle = models.CharField("Course Title", max_length=25)

    def __str__(self):
        return self.courseTitle


class Period(models.Model):
    #Using Django default key
    startTime = models.TimeField("Start Time")
    endTime = models.TimeField("End Time")
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
    meetingDays = models.CharField("Meeting Day", max_length=5, choices=DAY_CHOICES)

    def __str__(self):
        return str(self.meetingDays) + " " + str(self.startTime) + "-" + str(self.endTime)


class Section(models.Model):
    #Using SectionID as primary key
    sectionID = models.CharField("Section ID", max_length=4, primary_key=True)
    instructor = models.CharField("Instructor", max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    periods = models.ManyToManyField(Period)

    def __str__(self):
        return self.sectionID






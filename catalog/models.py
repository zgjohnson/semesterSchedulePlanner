from django.db import models

# Create your models here.


class Course(models.Model):
    # Using Course Number as primary key
    departmentID = models.CharField("Department ID", max_length=4)
    courseNumber = models.CharField("Course Number", max_length=4, primary_key=True)
    courseTitle = models.CharField("Course Title", max_length=255)

    def __str__(self):
        return self.courseTitle


class Period(models.Model):
    # Using Django default key
    startTime = models.TimeField("Start Time")
    endTime = models.TimeField("End Time")
    MEETING_DAY_CHOICES = [
        (MONDAY, 'M'),
        (TUESDAY, 'T'),
        (WEDNESDAY, 'W'),
        (THURSDAY, 'R'),
        (FRIDAY, 'F'),
        (MONWED, 'MW'),
        (MONWEDFRI, 'MWF'),
        (TUETHU, 'TR'),
        (MONTUEWEDTHUFRI, 'MWTWRF')
    ]
    meeting_day = models.CharField(
        max_length=10,
        choices=MEETING_DAY_CHOICES,
        default=" ",
    )

    def __str__(self):
        return str(self.meeting_day) + " " + str(self.startTime) + "-" + str(self.endTime)


class Section(models.Model):
    # Using SectionID as primary key
    sectionID = models.CharField("Section ID", max_length=4, primary_key=True)
    instructor = models.CharField("Instructor", max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    periods = models.ManyToManyField(Period)

    def __str__(self):
        return self.sectionID

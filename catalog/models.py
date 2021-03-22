from django.db import models

# Create your models here.


class Course(models.Model):
    # Using course_Number as primary key
    department_Number = models.CharField("Department Number", max_length=4, default=" ")
    course_Number = models.CharField("Course Number", max_length=4)
    course_Title = models.CharField("Course Title", max_length=255)

    def __str__(self):
        return self.course_Title


class Period(models.Model):
    # Using Django default key
    start_Time = models.TimeField("Start Time")
    end_Time = models.TimeField("End Time")
    MONDAY = 'M'
    TUESDAY = 'T'
    WEDNESDAY = 'W'
    THURSDAY = 'R'
    FRIDAY = 'F'
    MONWED = 'MW'
    MONWEDFRI = 'MWF'
    TUETHU = 'TR'
    MONTUEWEDTHUFRI = 'MWTWRF'
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
        return str(self.meeting_day) + " " + str(self.start_Time) + "-" + str(self.end_Time)


class Section(models.Model):
    # Using section_ID as primary key
    section_ID = models.CharField("Section ID", max_length=4)
    instructor = models.CharField("Instructor", max_length=255)
    course_Number = models.ForeignKey(Course, on_delete=models.CASCADE)
    periods = models.ManyToManyField(Period)

    def __str__(self):
        return self.section_ID

from django.db import models

# Create your models here.


class Course(models.Model):
    # Using course_Number as a primary key
    department_ID = models.CharField(max_length=4, default=" ")
    course_Number = models.CharField(max_length=10, primary_key=True)
    course_Title = models.CharField(max_length=255)

    def __str__(self):
        return self.course_Title


class Period(models.Model):
    # Using Django default key
    start_Time = models.TimeField()
    end_Time = models.TimeField()
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

    )

    def __str__(self):
        return str(self.meeting_day) + " " + str(self.start_Time) + "-" + str(self.end_Time)


class Section(models.Model):
    # Using section_ID as primary key
    #this cant be a primary key, The section ID is going to be used for other courses
    section_ID = models.CharField(max_length=20, primary_key=True)
    instructor = models.CharField(max_length=255)
    #Each course can have multiple sections but each section will be related to one course. That is what this foreign key is for
    #course_Number = models.ForeignKey(Course, on_delete=models.CASCADE)
    periods = models.ManyToManyField(Period)

    def __str__(self):
        return self.section_ID

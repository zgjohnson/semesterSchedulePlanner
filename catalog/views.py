from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .models import Section


# Create your views here.

@login_required
def homePage(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        return render(request, 'catalog/homePage.html', {'courses': courses})


@login_required
def viewCourse(request, course_pk):
    courses = get_object_or_404(Course, pk=course_pk)
    section = Section.objects.all()
    return render(request, 'catalog/viewCourse.html', {'courses': courses, 'sections': section})


def schedulePage(request):
    return render(request, 'catalog/schedulePage.html')

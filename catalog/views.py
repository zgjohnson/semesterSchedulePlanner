from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course


# Create your views here.

@login_required
def homePage(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        return render(request, 'catalog/homePage.html', {'courses': courses})


@login_required
def viewCourse(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    return render(request, 'catalog/viewCourse.html', {'course': course})


def schedulePage(request):
    return render(request, 'catalog/schedulePage.html')

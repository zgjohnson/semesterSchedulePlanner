from django.shortcuts import render

# Create your views here.

def allCourses(request):
    render(request, 'schedule/allCourses.html')
from django.shortcuts import render, get_object_or_404
from apps.models.course import Course

def course_list(request):
    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    lessons = course.lessons.all().order_by('order')
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})

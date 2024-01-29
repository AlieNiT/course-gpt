from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from edu.models import Course, CourseRate
from edu.serializers import CourseSerializer


@csrf_exempt
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return JsonResponse(serializer.data)
    else:
        return HttpResponse(status=405)


@csrf_exempt
def course_rate(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        course_rates = CourseRate.objects.filter(course=course)
        if course_rates.count() == 0:
            rate = -1
        else:
            rate = 0
            for cr in course_rates:
                rate += cr.rate
            rate /= course_rates.count()
        return JsonResponse({'rate': rate})
    else:
        return HttpResponse(status=405)

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from edu.models import Course, CourseRate, CourseEnrollment
from edu.serializers import CourseSerializer, UserSerializer


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
@login_required(login_url='/login/')
def get_user_info(request):
    if request.method != 'GET':
        return HttpResponse(status=405)
    user = request.user
    serializer = UserSerializer(user)
    print(user.__class__)
    return JsonResponse(serializer.data)


@csrf_exempt
@login_required(login_url='/login/')
def get_user_courses(request):
    if request.method != 'GET':
        return HttpResponse(status=405)
    user = request.user
    serializer = CourseSerializer(user.courses, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@login_required(login_url='/login/')
def course_enroll(request, pk):
    if request.method != 'POST':
        return HttpResponse(status=405)
    user = request.user
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        return HttpResponse('Course does not found', status=404)
    if CourseEnrollment.objects.filter(student=user, course=course).exists():
        return HttpResponse('You have enrolled this course before.', status=400)
    CourseEnrollment.objects.create(student=user, course=course)
    return HttpResponse('Enrolled successfully', status=201)


@csrf_exempt
@login_required(login_url='/login/')
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
    # elif request.method == 'POST':
        # TODO: Add create new rate in post
    else:
        return HttpResponse(status=405)


@csrf_exempt
def basic_login(request):
    if request.method == 'GET':
        return HttpResponse('You must login first.')
    if request.method != 'POST':
        return HttpResponse(status=405)
    try:
        username = request.POST["username"]
        password = request.POST["password"]
    except Exception:
        return HttpResponse('username and password are required.', status=400)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('Logged in successfully.', status=200)
    else:
        return HttpResponse('Unauthorized', status=401)


def basic_logout(request):
    logout(request)
    return HttpResponse('Logged out successfully.', status=200)

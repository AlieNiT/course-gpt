"""
URL configuration for course_gpt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from edu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', views.course_list),
    path('courses/<int:pk>/', views.course_detail),
    path('courses/<int:pk>/enroll', views.course_enroll),
    path('courses/<int:pk>/rate', views.course_rate),
    path('signup/', views.signup),
    path('login/', views.basic_login),
    path('logout/', views.basic_logout),
    path('whoami/', views.get_user_info),
    path('enrolls/', views.get_user_courses),
]

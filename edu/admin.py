from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from edu.models import User, Student, Teacher, Course, CourseEnrollment, Transaction, Bookmark, CourseRate

admin.site.register(User, UserAdmin)
admin.site.register(Student, UserAdmin)
admin.site.register(Teacher, UserAdmin)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'difficulty', 'estimate_days', 'maker']


@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'progress']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'paid_amount', 'received_amount', 'description']


@admin.register(CourseRate)
class CourseRateAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'rate', 'comment']


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['course_enrollment', 'position', 'note']

from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    balance = models.PositiveIntegerField(help_text='In Tomans', default=0)


class Student(User):
    pass


class Teacher(User):
    pass


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    date_created = models.DateTimeField(auto_now=True)
    paid_amount = models.PositiveIntegerField(help_text='In Tomans', default=0)
    received_amount = models.PositiveIntegerField(help_text='In Tomans', default=0)
    description = models.CharField(max_length=128)


class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    price = models.PositiveIntegerField(help_text='In Tomans')
    estimate_days = models.PositiveIntegerField()
    difficulty = models.PositiveIntegerField(
        help_text='From 1 to 5. 5 is the hardest.',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    file_url = models.URLField()
    maker = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name='made_courses')

    def __str__(self):
        return self.name


class CourseRate(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_rates')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='course_rates')
    date_created = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=256, blank=True, default='')
    rate = models.PositiveIntegerField(
        help_text='From 1 to 5. 5 is the best.',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )


class CourseEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    date_started = models.DateTimeField(auto_now=True)
    date_expired = models.DateTimeField(default=timezone.now() + timedelta(days=30))
    progress = models.PositiveIntegerField()
    bookmarks = models.ManyToManyField('Bookmark')
    conversation_file = models.FileField(upload_to='conversations')


class Bookmark(models.Model):
    course_enrollment = models.ForeignKey(CourseEnrollment, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    position = models.PositiveIntegerField()
    note = models.CharField(max_length=512)

from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

USER_TYPES = (
    ("STUDENT", "STUDENT"),
    ("TEACHER", "TEACHER"),
)


class User(AbstractUser):
    balance = models.PositiveIntegerField(help_text='In Tomans', default=0)
    type = models.CharField(choices=USER_TYPES, max_length=10)

    @property
    def courses(self):
        if self.type == 'STUDENT':
            return Course.objects.filter(enrollments__student=self)
        else:
            return Course.objects.filter(maker=self)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    date_created = models.DateTimeField(auto_now=True)
    paid_amount = models.PositiveIntegerField(help_text='In Tomans', default=0)
    received_amount = models.PositiveIntegerField(help_text='In Tomans', default=0)
    description = models.CharField(max_length=128)


class Course(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=1024)
    price = models.PositiveIntegerField(help_text='In Tomans')
    estimate_days = models.PositiveIntegerField()
    difficulty = models.PositiveIntegerField(
        help_text='From 1 to 5. 5 is the hardest.',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    file_url = models.URLField()
    picture = models.FilePathField(null=True, blank=True)
    maker = models.ForeignKey(User, on_delete=models.PROTECT, related_name='made_courses')

    def __str__(self):
        return self.name

    def clean(self):
        if self.maker.type != 'TEACHER':
            raise ValueError('only teachers can make courses.')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        super().save(force_insert, force_update, using, update_fields)


class CourseRate(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_rates')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_rates')
    date_created = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=256, blank=True, default='')
    rate = models.PositiveIntegerField(
        help_text='From 1 to 5. 5 is the best.',
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def clean(self):
        if self.student.type != 'STUDENT':
            raise ValueError('only students can rate courses.')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        super().save(force_insert, force_update, using, update_fields)


class CourseEnrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    date_started = models.DateTimeField(auto_now=True)
    progress = models.PositiveIntegerField(default=0)
    bookmarks = models.ManyToManyField('Bookmark')
    conversation_file = models.FileField(upload_to='conversations', null=True, blank=True)

    def clean(self):
        if self.student.type != 'STUDENT':
            raise ValueError('only students can enroll courses.')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        super().save(force_insert, force_update, using, update_fields)


class Bookmark(models.Model):
    course_enrollment = models.ForeignKey(CourseEnrollment, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    position = models.PositiveIntegerField()
    note = models.CharField(max_length=512)

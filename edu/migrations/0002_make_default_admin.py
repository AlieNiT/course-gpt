from django.contrib.auth.hashers import make_password
from django.db import migrations
from django.db.migrations.state import StateApps


def forward(apps: StateApps, schema_editor):
    User = apps.get_model('edu', 'User')  # noqa
    User.objects.get_or_create(username='admin', defaults={
        'password': make_password('admin'),
        'is_staff': True,
        'is_superuser': True,
    })


def backward(apps: StateApps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forward, backward)
    ]

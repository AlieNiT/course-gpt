# Generated by Django 4.2.8 on 2024-02-03 19:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0007_alter_courseenrollment_date_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseenrollment',
            name='conversation_file',
            field=models.FileField(blank=True, null=True, upload_to='conversations'),
        ),
        migrations.AlterField(
            model_name='courseenrollment',
            name='date_expired',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 4, 19, 44, 3, 89399, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='courseenrollment',
            name='progress',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 2.1.7 on 2019-05-30 13:05

import datetime
from django.db import migrations, models
import helps_student.models


class Migration(migrations.Migration):

    dependencies = [
        ('helps_student', '0003_auto_20190419_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='session_time',
        ),
        migrations.AddField(
            model_name='session',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 5, 30, 23, 5, 46, 597122)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='end_time',
            field=models.DateTimeField(default=helps_student.models.default_start_time),
        ),
        migrations.AddField(
            model_name='session',
            name='start_time',
            field=models.DateTimeField(default=helps_student.models.default_start_time),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_ID',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staffaccount',
            name='staff_id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentaccount',
            name='DOB',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='studentaccount',
            name='student_id',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='workshop_ID',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]
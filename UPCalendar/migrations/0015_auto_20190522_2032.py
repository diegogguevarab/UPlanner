# Generated by Django 2.2 on 2019-05-22 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPCalendar', '0014_auto_20190522_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sleepTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 28, 21, 0), null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='wakeUpTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 28, 7, 0), null=True),
        ),
    ]

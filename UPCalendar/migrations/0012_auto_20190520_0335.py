# Generated by Django 2.2 on 2019-05-20 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPCalendar', '0011_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='color',
            field=models.CharField(default='#325d88', max_length=7),
        ),
    ]

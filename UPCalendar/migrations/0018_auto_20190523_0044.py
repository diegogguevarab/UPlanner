# Generated by Django 2.2 on 2019-05-23 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UPCalendar', '0017_auto_20190523_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

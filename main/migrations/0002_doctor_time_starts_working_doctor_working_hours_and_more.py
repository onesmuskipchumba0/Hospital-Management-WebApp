# Generated by Django 5.0 on 2024-01-22 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='time_starts_working',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 8, 0)),
        ),
        migrations.AddField(
            model_name='doctor',
            name='working_hours',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 20, 29, 0, 109741)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 22, 20, 29, 0, 137956)),
        ),
    ]

# Generated by Django 4.2 on 2023-04-20 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0010_alter_appointment_end_alter_appointment_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 21, 9, 33, 537871), verbose_name='Appointment end time'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 21, 9, 33, 537871), verbose_name='Appointment start time'),
        ),
    ]
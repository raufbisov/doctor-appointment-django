# Generated by Django 4.2 on 2023-04-20 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_delete_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=True, verbose_name='Is user verified?'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField(verbose_name='Appointment title')),
                ('start_date', models.DateTimeField(verbose_name='Appointment start datetime')),
                ('end_date', models.DateTimeField(verbose_name='Appointment end datetime')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employee', to=settings.AUTH_USER_MODEL)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 4.2 on 2023-04-14 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_patient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Patient',
        ),
    ]

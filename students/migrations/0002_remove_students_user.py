# Generated by Django 4.2.5 on 2024-08-18 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='user',
        ),
    ]

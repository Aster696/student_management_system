# Generated by Django 4.2.5 on 2024-08-18 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='instructor',
            field=models.IntegerField(),
        ),
    ]

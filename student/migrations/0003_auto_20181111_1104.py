# Generated by Django 2.1.3 on 2018-11-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20181111_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-18 15:55

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('poll', '0007_auto_20210318_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='question_num',
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-17 23:55

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('poll', '0005_poll2_poll_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll2',
            name='poll_question',
        ),
    ]

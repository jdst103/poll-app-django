# Generated by Django 3.1.7 on 2021-03-21 02:59

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('poll', '0008_remove_poll_question_num'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Poll2',
            new_name='PollDetail',
        ),
        migrations.RenameModel(
            old_name='Poll',
            new_name='PollsList',
        ),
    ]

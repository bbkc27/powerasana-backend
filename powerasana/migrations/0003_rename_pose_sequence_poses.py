# Generated by Django 4.0.6 on 2022-07-07 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('powerasana', '0002_alter_pose_cues'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sequence',
            old_name='pose',
            new_name='poses',
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerasana', '0005_alter_pose_sequences 2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pose',
            name='sequences',
        ),
        migrations.RemoveField(
            model_name='sequence',
            name='user_string',
        ),
        migrations.AddField(
            model_name='sequence',
            name='poses',
            field=models.ManyToManyField(to='powerasana.pose'),
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerasana', '0003_sequence_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sequence',
            name='poses',
        ),
        migrations.AddField(
            model_name='pose',
            name='sequences',
            field=models.ManyToManyField(related_name='pose_list', to='powerasana.sequence'),
        ),
    ]

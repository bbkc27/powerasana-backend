# Generated by Django 4.0.6 on 2022-07-16 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerasana', '0006_remove_sequence_poses'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequence',
            name='poses',
            field=models.ManyToManyField(to='powerasana.pose'),
        ),
    ]

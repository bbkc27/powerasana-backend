# Generated by Django 4.0.6 on 2022-07-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('powerasana', '0007_sequence_poses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequence',
            name='poses',
            field=models.ManyToManyField(blank=True, related_name='sequence_list', to='powerasana.pose'),
        ),
    ]
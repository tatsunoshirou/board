# Generated by Django 2.1.4 on 2018-12-26 03:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_good'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Good',
        ),
        migrations.AddField(
            model_name='post',
            name='good_counts',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

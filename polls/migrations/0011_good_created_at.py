# Generated by Django 2.1.4 on 2019-01-23 02:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_remove_good_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
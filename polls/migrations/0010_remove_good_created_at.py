# Generated by Django 2.1.4 on 2019-01-23 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_good_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='created_at',
        ),
    ]

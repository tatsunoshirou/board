# Generated by Django 2.1.4 on 2019-01-23 05:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_remove_good_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='post',
        ),
        migrations.AddField(
            model_name='good',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Good'),
        ),
    ]

# Generated by Django 2.0.3 on 2018-03-20 17:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

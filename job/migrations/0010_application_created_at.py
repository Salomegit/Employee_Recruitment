# Generated by Django 4.1.5 on 2023-01-14 12:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_alter_job_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

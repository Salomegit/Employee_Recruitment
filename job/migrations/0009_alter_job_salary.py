# Generated by Django 4.1.5 on 2023-01-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
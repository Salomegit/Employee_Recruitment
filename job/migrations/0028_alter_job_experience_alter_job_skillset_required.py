# Generated by Django 4.1.5 on 2023-02-26 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0027_alter_job_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='skillset_required',
            field=models.TextField(max_length=2000),
        ),
    ]
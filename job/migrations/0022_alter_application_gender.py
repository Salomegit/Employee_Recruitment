# Generated by Django 4.1.5 on 2023-02-03 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0021_alter_job_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1, null=True),
        ),
    ]
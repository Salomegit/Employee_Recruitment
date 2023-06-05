# Generated by Django 4.2 on 2023-04-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0059_alter_application_level_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='level_education',
            field=models.CharField(choices=[('High School', 'High School'), ('Associate Degree', 'Associate Degree'), ('Bachelor Degree', "Bachelor's Degree"), ('Master Degree', "Master's Degree"), ('Doctorate', 'Doctoral Degree'), ('Professional Degree', 'Professional Degree'), ('Certificate', 'Certificate'), ('Diploma', 'Diploma')], max_length=30),
        ),
    ]
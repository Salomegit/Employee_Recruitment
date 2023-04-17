# Generated by Django 4.2 on 2023-04-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0053_application_level_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='level_education',
            field=models.CharField(choices=[('certificate', 'Certificate'), ('diploma', 'Diploma'), ("associate's degree", "Associate's Degree"), ("bachelor's degree", "Bachelor's Degree"), ("master's degree", "Master's Degree"), ('doctorate', 'Doctorate'), ('high_school', 'High School'), ('professional degree', 'Profesional Degree')], max_length=30, null=True),
        ),
    ]
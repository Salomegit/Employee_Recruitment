# Generated by Django 4.1.5 on 2023-01-16 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_application_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-15 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_application_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='education',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Education'),
        ),
    ]
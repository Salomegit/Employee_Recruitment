# Generated by Django 4.1.7 on 2023-03-30 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0046_alter_job_skillset_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='education',
            field=models.CharField(blank=True, max_length=2553, null=True),
        ),
    ]

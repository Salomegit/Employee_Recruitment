# Generated by Django 4.1.5 on 2023-03-01 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0031_remove_application_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='department_name',
            field=models.CharField(choices=[('CSS', 'Computer Support Specialist'), ('HWA', 'Hardware Engineer'), ('CSA', 'Computer System Analyst '), ('SWD', 'Software Developer'), ('PRG', 'Programmer'), ('WBD', 'Web developer'), ('NWE', 'Network engineer'), ('SWT', 'Software Tester')], max_length=4),
        ),
    ]

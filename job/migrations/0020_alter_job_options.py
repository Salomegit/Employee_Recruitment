# Generated by Django 4.1.5 on 2023-01-25 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0019_alter_application_education'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['created_at']},
        ),
    ]

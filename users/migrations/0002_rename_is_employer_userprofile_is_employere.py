# Generated by Django 4.1.5 on 2023-01-23 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_employer',
            new_name='is_employere',
        ),
    ]

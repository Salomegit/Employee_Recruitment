# Generated by Django 4.1.5 on 2023-01-24 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_is_employer_userprofile_is_employere'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_employere',
            new_name='is_employer',
        ),
    ]

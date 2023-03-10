# Generated by Django 4.1.5 on 2023-01-25 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0020_alter_job_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_rename_is_employere_userprofile_is_employer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConversationMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversationmessages', to='job.application')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversationmessages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]

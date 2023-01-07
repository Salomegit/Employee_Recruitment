# Generated by Django 4.1.4 on 2023-01-07 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='skillset_required',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('experience', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='job.job')),
            ],
        ),
    ]

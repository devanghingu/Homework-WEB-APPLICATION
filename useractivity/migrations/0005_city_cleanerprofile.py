# Generated by Django 3.0.2 on 2020-02-05 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useractivity', '0004_user_is_cleaner'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CleanerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality_score', models.IntegerField(default=0)),
                ('total_completed_job', models.IntegerField(default=0)),
                ('working_time_slot', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('working_city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='useractivity.City')),
            ],
        ),
    ]

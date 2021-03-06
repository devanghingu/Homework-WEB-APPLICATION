# Generated by Django 3.0.2 on 2020-02-05 12:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('useractivity', '0005_city_cleanerprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='Address')),
                ('dateofcleaning', models.DateField(verbose_name='Date Of Cleaning')),
                ('timeslot', models.CharField(max_length=50)),
                ('notes', models.TextField()),
                ('job_complated', models.BooleanField(default=False, verbose_name='job Completed')),
                ('city', models.ManyToManyField(to='useractivity.City', verbose_name='customer city')),
                ('cleaner_id', models.ManyToManyField(to='useractivity.CleanerProfile')),
                ('customer_id', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

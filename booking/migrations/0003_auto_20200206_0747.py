# Generated by Django 3.0.2 on 2020-02-06 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useractivity', '0005_city_cleanerprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0002_auto_20200206_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Address'),
        ),
        migrations.RemoveField(
            model_name='bookings',
            name='city',
        ),
        migrations.AddField(
            model_name='bookings',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='useractivity.City'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='bookings',
            name='cleaner_id',
        ),
        migrations.AddField(
            model_name='bookings',
            name='cleaner_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='useractivity.CleanerProfile'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='bookings',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='bookings',
            name='customer_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookings',
            name='dateofcleaning',
            field=models.DateField(auto_now_add=True, verbose_name='Date Of Cleaning'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='any message to cleaner '),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='timeslot',
            field=models.IntegerField(choices=[(1, '10 AM - 12 PM'), (2, '12 PM - 02 PM'), (3, '02 PM - 04 PM'), (4, '04 PM - 06 PM'), (5, '06 PM - 08 PM')]),
        ),
    ]

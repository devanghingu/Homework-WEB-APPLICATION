# Generated by Django 3.0.2 on 2020-02-05 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useractivity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.CharField(help_text='Your Contact number must be in numbers', max_length=12, unique=True),
        ),
    ]

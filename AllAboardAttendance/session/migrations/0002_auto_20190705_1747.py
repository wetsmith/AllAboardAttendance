# Generated by Django 2.2.1 on 2019-07-06 00:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendant',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 6, 0, 47, 3, 326535, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='diredge',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 6, 0, 47, 3, 326535, tzinfo=utc), verbose_name='date connection made'),
        ),
    ]
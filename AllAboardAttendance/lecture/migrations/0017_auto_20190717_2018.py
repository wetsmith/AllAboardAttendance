# Generated by Django 2.2.1 on 2019-07-18 03:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0016_auto_20190717_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendant',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 3, 18, 23, 844940, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='diredge',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 3, 18, 23, 845940, tzinfo=utc), verbose_name='date connection made'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 3, 18, 23, 803954, tzinfo=utc), verbose_name='date published'),
        ),
    ]
# Generated by Django 2.2.1 on 2019-07-18 03:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0015_auto_20190717_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendant',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 3, 17, 12, 109802, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='diredge',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 3, 17, 12, 110802, tzinfo=utc), verbose_name='date connection made'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 3, 17, 12, 70814, tzinfo=utc), verbose_name='date published'),
        ),
    ]

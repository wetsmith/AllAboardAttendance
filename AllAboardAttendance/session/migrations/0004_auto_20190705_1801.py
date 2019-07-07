# Generated by Django 2.2.1 on 2019-07-06 01:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_auto_20190705_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendant',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 6, 1, 1, 57, 193495, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='diredge',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 6, 1, 1, 57, 193495, tzinfo=utc), verbose_name='date connection made'),
        ),
    ]
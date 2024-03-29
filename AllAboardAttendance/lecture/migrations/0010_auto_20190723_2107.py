# Generated by Django 2.2.1 on 2019-07-24 04:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0009_auto_20190723_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendant',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 4, 7, 28, 667958, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='diredge',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 4, 7, 28, 667958, tzinfo=utc), verbose_name='date connection made'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 4, 7, 28, 628960, tzinfo=utc), verbose_name='date published'),
        ),
    ]

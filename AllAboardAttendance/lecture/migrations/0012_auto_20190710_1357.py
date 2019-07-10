# Generated by Django 2.2.1 on 2019-07-10 20:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0011_auto_20190710_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendant',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 20, 57, 51, 659754, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='diredge',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 20, 57, 51, 660752, tzinfo=utc), verbose_name='date connection made'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 20, 57, 51, 617839, tzinfo=utc), verbose_name='date published'),
        ),
    ]

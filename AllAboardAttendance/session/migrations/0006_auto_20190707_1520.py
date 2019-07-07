# Generated by Django 2.2.3 on 2019-07-07 22:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0005_auto_20190707_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendant',
            name='temp_id',
            field=models.CharField(default='no code', max_length=20),
        ),
        migrations.AlterField(
            model_name='attendant',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 7, 22, 20, 57, 891025, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='diredge',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 7, 22, 20, 57, 891524, tzinfo=utc), verbose_name='date connection made'),
        ),
        migrations.AlterField(
            model_name='session',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 7, 22, 20, 57, 813877, tzinfo=utc), verbose_name='date published'),
        ),
    ]

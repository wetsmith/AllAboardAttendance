# Generated by Django 2.2.1 on 2019-07-18 03:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_auto_20190717_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 3, 3, 3, 581361, tzinfo=utc), verbose_name='date published'),
        ),
    ]

# Generated by Django 2.2.1 on 2019-07-14 04:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_auto_20190713_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 14, 4, 10, 40, 81264, tzinfo=utc), verbose_name='date published'),
        ),
    ]

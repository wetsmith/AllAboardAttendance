# Generated by Django 2.2.1 on 2019-07-14 05:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_auto_20190713_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 14, 5, 13, 12, 478614, tzinfo=utc), verbose_name='date published'),
        ),
    ]
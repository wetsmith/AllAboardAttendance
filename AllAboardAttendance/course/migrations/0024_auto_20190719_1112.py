# Generated by Django 2.2.3 on 2019-07-19 18:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_auto_20190718_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 19, 18, 12, 6, 839807, tzinfo=utc), verbose_name='date published'),
        ),
    ]

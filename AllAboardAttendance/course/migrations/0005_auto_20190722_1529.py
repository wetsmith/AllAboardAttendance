# Generated by Django 2.2.1 on 2019-07-22 22:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20190722_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 22, 22, 29, 17, 389111, tzinfo=utc), verbose_name='date published'),
        ),
    ]

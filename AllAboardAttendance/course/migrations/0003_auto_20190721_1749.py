# Generated by Django 2.2.1 on 2019-07-22 00:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20190721_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 22, 0, 49, 47, 396957, tzinfo=utc), verbose_name='date published'),
        ),
    ]

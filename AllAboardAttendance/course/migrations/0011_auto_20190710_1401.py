# Generated by Django 2.2.1 on 2019-07-10 21:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20190710_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 21, 1, 18, 622406, tzinfo=utc), verbose_name='date published'),
        ),
    ]
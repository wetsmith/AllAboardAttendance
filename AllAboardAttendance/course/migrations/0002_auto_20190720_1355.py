# Generated by Django 2.2.3 on 2019-07-20 20:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 20, 20, 55, 1, 33156, tzinfo=utc), verbose_name='date published'),
        ),
    ]
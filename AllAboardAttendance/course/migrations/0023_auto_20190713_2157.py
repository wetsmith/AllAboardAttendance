# Generated by Django 2.2.1 on 2019-07-14 04:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_merge_20190713_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 14, 4, 57, 18, 965574, tzinfo=utc), verbose_name='date published'),
        ),
    ]
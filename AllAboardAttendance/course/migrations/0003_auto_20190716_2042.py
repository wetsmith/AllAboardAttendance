# Generated by Django 2.2.3 on 2019-07-17 03:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20190715_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 17, 3, 42, 22, 461671, tzinfo=utc), verbose_name='date published'),
        ),
    ]
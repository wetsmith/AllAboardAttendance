# Generated by Django 2.2.3 on 2019-07-10 01:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='student_ids',
            new_name='student',
        ),
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 1, 44, 18, 637053, tzinfo=utc), verbose_name='date published'),
        ),
    ]

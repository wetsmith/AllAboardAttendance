# Generated by Django 2.2.1 on 2019-07-18 02:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0011_auto_20190717_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='lecture_qr_path',
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_qr',
            field=models.ImageField(editable=False, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='attendant',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 2, 27, 32, 141465, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='diredge',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 2, 27, 32, 142465, tzinfo=utc), verbose_name='date connection made'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 2, 27, 32, 102477, tzinfo=utc), verbose_name='date published'),
        ),
    ]

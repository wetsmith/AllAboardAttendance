# Generated by Django 2.2.1 on 2019-07-18 02:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0012_auto_20190717_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendant',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 2, 56, 3, 978832, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='diredge',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 2, 56, 3, 979826, tzinfo=utc), verbose_name='date connection made'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lecture_qr',
            field=models.ImageField(null=True, upload_to='qrcode/'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 2, 56, 3, 941828, tzinfo=utc), verbose_name='date published'),
        ),
    ]

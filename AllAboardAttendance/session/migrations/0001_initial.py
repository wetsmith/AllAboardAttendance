# Generated by Django 2.2.1 on 2019-07-06 00:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20)),
                ('position', models.CharField(default='N/A', max_length=20)),
                ('connections', models.IntegerField(default=-1)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2019, 7, 6, 0, 13, 57, 385582, tzinfo=utc), verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='DirEdge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2019, 7, 6, 0, 13, 57, 385582, tzinfo=utc), verbose_name='date connection made')),
                ('direction_id', models.CharField(max_length=20)),
                ('attendant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='session.Attendant')),
            ],
        ),
        migrations.AddField(
            model_name='attendant',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.Session'),
        ),
    ]
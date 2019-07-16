# Generated by Django 2.2.3 on 2019-07-16 03:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20)),
                ('temp_id', models.CharField(default='no code', max_length=20)),
                ('position', models.CharField(default='N/A', max_length=20)),
                ('connections', models.IntegerField(default=-1)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2019, 7, 16, 3, 41, 0, 159376, tzinfo=utc), verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_title', models.CharField(default='default', max_length=20)),
                ('lecture_title_slug', models.SlugField(editable=False, max_length=20, null=True, unique=True)),
                ('lecture_key', models.CharField(default='default', max_length=20)),
                ('lecture_key_slug', models.SlugField(editable=False, max_length=20, null=True, unique=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2019, 7, 16, 3, 41, 0, 106706, tzinfo=utc), verbose_name='date published')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='DirEdge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2019, 7, 16, 3, 41, 0, 159376, tzinfo=utc), verbose_name='date connection made')),
                ('direction_id', models.CharField(max_length=20)),
                ('attendant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lecture.Attendant')),
            ],
        ),
        migrations.AddField(
            model_name='attendant',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecture.Lecture'),
        ),
    ]

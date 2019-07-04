# Generated by Django 2.2.3 on 2019-07-04 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ID', models.CharField(max_length=20)),
                ('connections', models.IntegerField(default=-1)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
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
                ('pub_date', models.DateTimeField(verbose_name='date connection made')),
                ('directionID', models.CharField(max_length=20)),
                ('attendent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sessions.Attendent')),
            ],
        ),
        migrations.AddField(
            model_name='attendent',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sessions.Session'),
        ),
    ]

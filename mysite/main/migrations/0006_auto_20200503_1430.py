# Generated by Django 3.0.3 on 2020-05-03 14:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200503_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='hack',
            name='hack_series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.HackSeries', verbose_name='Series'),
        ),
        migrations.AddField(
            model_name='hackseries',
            name='hack_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.HackCategory', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='hack',
            name='hack_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 14, 30, 13, 969104), verbose_name='date published'),
        ),
    ]

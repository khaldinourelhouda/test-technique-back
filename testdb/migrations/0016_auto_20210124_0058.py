# Generated by Django 3.1 on 2021-01-23 23:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0015_auto_20210122_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur_test',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 24, 0, 58, 23, 70097)),
        ),
    ]

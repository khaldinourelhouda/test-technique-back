# Generated by Django 3.1 on 2020-10-12 04:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0004_auto_20201006_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur_test',
            name='nb_questions_repondues',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='utilisateur_test',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 12, 5, 16, 43, 633464)),
        ),
    ]
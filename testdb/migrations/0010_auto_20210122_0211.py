# Generated by Django 3.1 on 2021-01-22 01:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testdb', '0009_auto_20210122_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choix_utilisateur',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='utilisateur_test',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 22, 2, 11, 49, 730046)),
        ),
        migrations.AlterField(
            model_name='utilisateur_test',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Utilisateur',
        ),
    ]

# Generated by Django 2.2.7 on 2020-01-02 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20200102_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='day',
            field=models.CharField(default=datetime.date(2020, 1, 2), max_length=15),
        ),
    ]
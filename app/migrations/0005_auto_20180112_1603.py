# Generated by Django 2.0 on 2018-01-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180112_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coinshot',
            name='price',
        ),
        migrations.AddField(
            model_name='coinshot',
            name='value',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=16, verbose_name='Value'),
        ),
    ]
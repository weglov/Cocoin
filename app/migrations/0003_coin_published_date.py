# Generated by Django 2.0 on 2018-01-02 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180102_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
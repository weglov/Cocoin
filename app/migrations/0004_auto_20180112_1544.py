# Generated by Django 2.0 on 2018-01-12 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_coinhistory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoinHistory',
            new_name='CoinShot',
        ),
    ]

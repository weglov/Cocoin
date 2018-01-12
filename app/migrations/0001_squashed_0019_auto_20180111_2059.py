# Generated by Django 2.0 on 2018-01-12 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('app', '0001_initial'), ('app', '0002_auto_20180102_2241'), ('app', '0003_coin_published_date'), ('app', '0004_auto_20180103_1301'), ('app', '0005_remove_coin_logo'), ('app', '0006_auto_20180103_1304'), ('app', '0007_auto_20180103_1536'), ('app', '0008_auto_20180103_1549'), ('app', '0009_auto_20180103_1604'), ('app', '0010_auto_20180103_1606'), ('app', '0011_auto_20180103_1610'), ('app', '0012_auto_20180103_1810'), ('app', '0013_auto_20180103_1812'), ('app', '0014_auto_20180104_1017'), ('app', '0015_auto_20180104_1020'), ('app', '0016_asset'), ('app', '0017_auto_20180105_1122'), ('app', '0018_auto_20180107_2031'), ('app', '0019_auto_20180111_2059')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=3, default=0, max_digits=16, verbose_name='Price')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Logo')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Coin')),
                ('value', models.DecimalField(decimal_places=8, max_digits=16, verbose_name='Value')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(choices=[('Mobile', 'Mobile'), ('Web', 'Web'), ('Desktop', 'Desktop')], default='Desktop', max_length=16, verbose_name='Device')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Info')),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='wallet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Wallet'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.4 on 2018-06-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ram', '0006_auto_20180618_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory_info',
            name='series',
            field=models.CharField(blank=True, default='---', max_length=50),
        ),
        migrations.AlterField(
            model_name='memory_info',
            name='asin',
            field=models.CharField(blank=True, default='---', max_length=100, verbose_name='ASIN'),
        ),
    ]

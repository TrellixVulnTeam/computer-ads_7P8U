# Generated by Django 2.0.4 on 2018-05-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainboard', '0003_auto_20180526_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainboard_info',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]

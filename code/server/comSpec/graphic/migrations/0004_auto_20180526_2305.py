# Generated by Django 2.0.4 on 2018-05-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphic', '0003_auto_20180526_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphic_info',
            name='mem_bandwidth',
            field=models.CharField(help_text='Unit: MB/s', max_length=10, verbose_name='Memory Bandwidth'),
        ),
    ]

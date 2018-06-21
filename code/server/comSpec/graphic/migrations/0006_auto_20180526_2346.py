# Generated by Django 2.0.4 on 2018-05-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphic', '0005_auto_20180526_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphic_info',
            name='power',
            field=models.CharField(blank=True, help_text='Unit: W', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='graphic_info',
            name='recom_power',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Recommending Power'),
        ),
    ]

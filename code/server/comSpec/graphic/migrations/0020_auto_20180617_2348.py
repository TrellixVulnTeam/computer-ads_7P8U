# Generated by Django 2.0.4 on 2018-06-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphic', '0019_auto_20180617_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api_supp',
            name='version',
            field=models.CharField(blank=True, default=' ', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='graphic_info',
            name='boost_clock',
            field=models.CharField(blank=True, default='---', help_text='**Unit :MHz', max_length=50),
        ),
        migrations.AlterField(
            model_name='graphic_info',
            name='core_clock',
            field=models.CharField(blank=True, default='---', help_text='**Unit :MHz', max_length=50),
        ),
        migrations.AlterField(
            model_name='graphic_info',
            name='power',
            field=models.CharField(blank=True, default='---', help_text='**Unit: W', max_length=30),
        ),
        migrations.AlterField(
            model_name='graphic_info',
            name='recom_power',
            field=models.CharField(blank=True, default='---', help_text='**Unit: W', max_length=30, verbose_name='Recommending Power'),
        ),
    ]

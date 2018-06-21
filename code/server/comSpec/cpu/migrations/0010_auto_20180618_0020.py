# Generated by Django 2.0.4 on 2018-06-17 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpu', '0009_auto_20180617_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu_info',
            name='base_fr',
            field=models.CharField(help_text='**Unit: GHz', max_length=50, verbose_name='Base Frequency'),
        ),
        migrations.AlterField(
            model_name='cpu_info',
            name='cache',
            field=models.CharField(default='---', help_text='**Unit: MB', max_length=100, verbose_name='Cache'),
        ),
        migrations.AlterField(
            model_name='cpu_info',
            name='cmos',
            field=models.CharField(default='---', help_text='**Unit: nm or ELSE', max_length=50, verbose_name='CMOS'),
        ),
        migrations.AlterField(
            model_name='cpu_info',
            name='max_mem_bandwidth',
            field=models.CharField(blank=True, default='---', help_text='**Unit: MB/s or GB/s', max_length=50, verbose_name='Max Memory bandwidth'),
        ),
        migrations.AlterField(
            model_name='cpu_info',
            name='max_memory',
            field=models.CharField(blank=True, default='---', help_text='Unit: MB', max_length=100),
        ),
        migrations.AlterField(
            model_name='cpu_info',
            name='name',
            field=models.CharField(help_text='Ex: Intel Core i5-3470.', max_length=100),
        ),
        migrations.AlterField(
            model_name='cpu_info',
            name='num_of_thread',
            field=models.CharField(blank=True, default='---', max_length=100, verbose_name='Number of Threads'),
        ),
        migrations.AlterField(
            model_name='cpu_info',
            name='tdp',
            field=models.CharField(default='---', help_text='**Unit: W', max_length=50, verbose_name='Power Consumtion'),
        ),
    ]
# Generated by Django 2.0.4 on 2018-05-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainboard_info',
            name='expand_slot_des',
            field=models.TextField(max_length=2000, verbose_name='Expansion Slot Description'),
        ),
    ]
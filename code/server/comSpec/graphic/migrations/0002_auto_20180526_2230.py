# Generated by Django 2.0.4 on 2018-05-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphic_info',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

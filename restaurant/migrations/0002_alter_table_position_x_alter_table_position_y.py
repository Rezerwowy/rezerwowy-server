# Generated by Django 4.2.2 on 2023-06-15 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='position_x',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='table',
            name='position_y',
            field=models.IntegerField(default=0),
        ),
    ]

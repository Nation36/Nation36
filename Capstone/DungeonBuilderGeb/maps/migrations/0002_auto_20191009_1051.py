# Generated by Django 2.2.6 on 2019-10-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='background',
            field=models.FilePathField(path='/static/background_images'),
        ),
    ]

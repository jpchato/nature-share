# Generated by Django 3.1 on 2020-12-03 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natureShareApp', '0002_auto_20201203_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='organism',
            name='picture',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]

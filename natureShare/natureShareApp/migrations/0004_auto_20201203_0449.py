# Generated by Django 3.1 on 2020-12-03 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natureShareApp', '0003_organism_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organism',
            name='ecosystem',
            field=models.CharField(blank=True, choices=[('Temperate Rainforest', 'Temperate Rainforest'), ('Tropical Rainforest', 'Tropical Rainforest'), ('DESERT', 'Desert'), ('Grassland', 'Grassland'), ('Taiga', 'Taiga'), ('Tundra', 'Tundra'), ('Chaparral', 'Chaparral'), ('Ocean', 'Ocean'), ('Unknown', 'Unknown'), ('Other', 'Other')], max_length=255, null=True),
        ),
    ]

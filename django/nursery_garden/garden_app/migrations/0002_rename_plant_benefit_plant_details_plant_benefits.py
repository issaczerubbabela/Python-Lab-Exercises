# Generated by Django 5.0.3 on 2024-10-16 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant_details',
            old_name='plant_benefit',
            new_name='plant_benefits',
        ),
    ]

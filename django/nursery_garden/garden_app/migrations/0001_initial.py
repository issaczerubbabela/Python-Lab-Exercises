# Generated by Django 5.0.3 on 2024-10-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=20)),
                ('plant_type', models.CharField(max_length=20)),
                ('plant_price', models.IntegerField()),
                ('plant_benefit', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-23 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErshouHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduce', models.CharField(max_length=30)),
                ('house_address', models.CharField(max_length=30)),
                ('house_floor', models.CharField(max_length=10)),
                ('house_square', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ershou_type', models.CharField(max_length=10)),
                ('built_time', models.CharField(max_length=10)),
                ('house_orientations', models.CharField(max_length=5)),
                ('single_price', models.IntegerField()),
                ('total_price', models.IntegerField()),
            ],
        ),
    ]

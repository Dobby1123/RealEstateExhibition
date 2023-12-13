# Generated by Django 4.0.5 on 2022-06-23 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_introduce', models.CharField(max_length=20)),
                ('rent_address', models.CharField(max_length=20)),
                ('rent_style', models.CharField(max_length=10)),
                ('rent_square', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rent_orientations', models.CharField(max_length=5)),
                ('month_price', models.IntegerField()),
            ],
        ),
    ]
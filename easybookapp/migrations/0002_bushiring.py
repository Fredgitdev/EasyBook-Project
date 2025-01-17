# Generated by Django 5.1.3 on 2024-12-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easybookapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusHiring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('pick_up_location', models.CharField(max_length=200)),
                ('drop_off_location', models.CharField(max_length=200)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('contact', models.CharField(max_length=15)),
                ('bus_type', models.CharField(max_length=200)),
                ('seat_capacity', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-09 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_carbrand_carmanufacturer_sparepart_delete_car_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbrand',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='sparepart',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='sparepart',
            name='description',
        ),
    ]

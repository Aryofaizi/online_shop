# Generated by Django 4.2.4 on 2023-10-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_address_order_note_order_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=300, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=700, verbose_name='Order Note'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Phone Number'),
        ),
    ]

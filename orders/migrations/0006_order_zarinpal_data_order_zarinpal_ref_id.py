# Generated by Django 4.2.4 on 2023-10-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_zarinpal_authority_alter_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='zarinpal_data',
            field=models.TextField(blank=True, verbose_name='zarinpal data'),
        ),
        migrations.AddField(
            model_name='order',
            name='zarinpal_ref_id',
            field=models.CharField(blank=True, max_length=150, verbose_name='ref id'),
        ),
    ]

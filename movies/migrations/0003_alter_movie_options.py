# Generated by Django 4.2.4 on 2023-09-30 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ('title',)},
        ),
    ]

# Generated by Django 4.2.1 on 2023-08-09 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feetfirstapi', '0004_rename_is_completed_order_open_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_placed',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='open',
            field=models.BooleanField(default=True),
        ),
    ]
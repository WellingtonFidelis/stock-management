# Generated by Django 4.2.5 on 2023-10-21 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_management', '0005_alter_stock_category_alter_stock_item_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='export_to_CSV',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='last_updated',
        ),
    ]

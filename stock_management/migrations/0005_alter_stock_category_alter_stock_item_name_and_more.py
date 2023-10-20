# Generated by Django 4.2.5 on 2023-10-19 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_management', '0004_alter_category_name_alter_stock_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stock_management.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(default='0', null=True, verbose_name='Quantidade'),
        ),
    ]
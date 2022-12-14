# Generated by Django 4.1.4 on 2022-12-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('products', '0002_remove_product_categories_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='products', to='categories.category'),
        ),
    ]

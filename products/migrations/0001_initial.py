# Generated by Django 4.1.4 on 2022-12-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('image', models.CharField(max_length=300)),
                ('categories', models.ManyToManyField(related_name='products', to='categories.category')),
            ],
        ),
    ]

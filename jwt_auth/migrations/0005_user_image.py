# Generated by Django 4.1.4 on 2022-12-16 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0004_alter_user_postcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]

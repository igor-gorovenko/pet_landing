# Generated by Django 4.2.2 on 2023-07-05 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_remove_order_data_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='create_order',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='req_items',
            name='cart_items',
            field=models.ManyToManyField(to='cart.cart_items'),
        ),
    ]
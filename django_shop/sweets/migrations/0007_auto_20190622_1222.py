# Generated by Django 2.2.2 on 2019-06-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweets', '0006_cart_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='sweets.CartItem'),
        ),
    ]

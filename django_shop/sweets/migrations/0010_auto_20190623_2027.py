# Generated by Django 2.2.2 on 2019-06-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweets', '0009_auto_20190622_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')], default='Самовывоз', max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Принят в обработку', 'Принят в обработку'), ('Выполняется', 'Выполняется'), ('Оплачен', 'Оплачен')], default='Принят в обработку', max_length=100),
        ),
    ]

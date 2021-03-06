# Generated by Django 3.2.13 on 2022-07-27 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_order_cartid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cartid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cart'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.order'),
        ),
    ]

# Generated by Django 3.2.13 on 2022-07-26 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20220724_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cartid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.cart'),
            preserve_default=False,
        ),
    ]

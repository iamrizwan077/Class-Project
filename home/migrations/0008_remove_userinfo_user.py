# Generated by Django 3.2.13 on 2022-07-23 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
    ]
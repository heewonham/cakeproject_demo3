# Generated by Django 3.2.7 on 2021-09-18 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeManage', '0002_cake_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='price',
            field=models.CharField(default='10000원', max_length=100),
        ),
    ]

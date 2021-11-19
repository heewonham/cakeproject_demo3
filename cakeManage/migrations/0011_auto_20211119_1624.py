# Generated by Django 3.2.9 on 2021-11-19 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakeManage', '0010_alter_cake_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='referred_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cake', to='cakeManage.store'),
        ),
        migrations.AlterField(
            model_name='store',
            name='price',
            field=models.CharField(default='0', max_length=100),
        ),
    ]

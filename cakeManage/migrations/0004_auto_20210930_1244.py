# Generated by Django 3.2.5 on 2021-09-30 03:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakeManage', '0003_auto_20210929_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount_coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cakeManage.amountcoupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='pay_price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)]),
        ),
        migrations.AddField(
            model_name='order',
            name='percent_coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cakeManage.percentcoupon'),
        ),
    ]
# Generated by Django 3.2 on 2022-02-12 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cakeManage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='store',
            name='users_liked',
            field=models.ManyToManyField(blank=True, related_name='users_liked_store', related_query_name='users_liked_store', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cakeManage.order'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='percentcoupon',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordertransaction',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeManage.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='amount_coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cakeManage.amountcoupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='percent_coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cakeManage.percentcoupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='referred_cake',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeManage.cake', verbose_name='선택 케이크'),
        ),
        migrations.AddField(
            model_name='order',
            name='referred_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeManage.store', verbose_name='가게'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='주문자'),
        ),
        migrations.AddField(
            model_name='cake',
            name='referred_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cake', to='cakeManage.store'),
        ),
        migrations.AddField(
            model_name='cake',
            name='users_liked',
            field=models.ManyToManyField(blank=True, related_name='users_liked_cake', related_query_name='users_liked_cake', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='amountcoupon',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 3.2.5 on 2021-09-28 10:13

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cakeManage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='레터링위치',
        ),
        migrations.RemoveField(
            model_name='order',
            name='희망픽업시간',
        ),
        migrations.RemoveField(
            model_name='order',
            name='희망픽업일',
        ),
        migrations.AddField(
            model_name='cake',
            name='price',
            field=models.IntegerField(default=90000, validators=[django.core.validators.MinValueValidator(0, django.core.validators.MaxValueValidator(100000))]),
        ),
        migrations.AddField(
            model_name='order',
            name='lettering_position',
            field=models.CharField(choices=[('판 위에 레터링', '판 위에 레터링'), ('케이크에 직접 레터링', '케이크에 직접 레터링')], default='케이크에 직접 레터링', max_length=30, null=True, verbose_name='레터링 위치'),
        ),
        migrations.AddField(
            model_name='order',
            name='pickup_date',
            field=models.CharField(default=datetime.date.today, max_length=30, null=True, verbose_name='희망 픽업일'),
        ),
        migrations.AddField(
            model_name='order',
            name='pickup_time',
            field=models.CharField(choices=[('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00'), ('18:30', '18:30')], default='10:00', max_length=30, null=True, verbose_name='희망 시간'),
        ),
        migrations.CreateModel(
            name='PercentCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('use_from', models.DateTimeField(auto_now_add=True)),
                ('use_to', models.DateTimeField()),
                ('percent', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('is_active', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AmountCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('use_from', models.DateTimeField(auto_now_add=True)),
                ('use_to', models.DateTimeField()),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000)])),
                ('is_active', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-02 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=500)),
            ],
        ),
        migrations.CreateModel(
            name='MakePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, null=True, unique=True)),
                ('bank', models.CharField(max_length=5, null=True)),
                ('account_number', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.CharField(max_length=100, null=True, unique=True)),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.makepayment')),
            ],
        ),
    ]

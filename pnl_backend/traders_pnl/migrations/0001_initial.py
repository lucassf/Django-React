# Generated by Django 4.0.5 on 2022-06-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TradersPnl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trader_name', models.CharField(max_length=50)),
                ('trading_pnl', models.FloatField()),
                ('position_pnl', models.FloatField()),
            ],
        ),
    ]

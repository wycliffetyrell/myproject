# Generated by Django 3.0.5 on 2020-04-19 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20200419_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertotalprice',
            name='order_total',
            field=models.DecimalField(decimal_places=2, max_digits=65),
        ),
    ]

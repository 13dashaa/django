# Generated by Django 4.2.10 on 2024-08-20 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_balance_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]

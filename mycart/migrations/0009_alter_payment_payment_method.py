# Generated by Django 5.0.6 on 2024-06-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0008_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(max_length=20, null=True),
        ),
    ]

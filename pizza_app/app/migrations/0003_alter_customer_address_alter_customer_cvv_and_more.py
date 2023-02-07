# Generated by Django 4.1.5 on 2023-02-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_customer_cvv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(default='Your Address Here', max_length=256),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cvv',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='Your Name Here', max_length=256),
        ),
    ]

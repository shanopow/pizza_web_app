# Generated by Django 4.1.5 on 2023-02-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_customer_address_alter_customer_cvv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='cheese',
            field=models.CharField(choices=[('Small', 'SMALL'), ('Medium', 'MEDIUM'), ('Large', 'LARGE')], default='Mozzarella', max_length=10),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='crust',
            field=models.CharField(choices=[('Normal', 'NORMAL'), ('Thin', 'THIN'), ('Thick', 'THICK'), ('Gluten free', 'GLUTEN FREE')], default='Normal', max_length=11),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='sauce',
            field=models.CharField(choices=[('Tomato', 'TOMATO'), ('Bbq', 'BBQ')], default='Tomato', max_length=6),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('Small', 'SMALL'), ('Medium', 'MEDIUM'), ('Large', 'LARGE')], default='Medium', max_length=6),
        ),
    ]

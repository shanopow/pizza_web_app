# Generated by Django 4.1.6 on 2023-02-06 22:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(default='Your Name Here')),
                ('address', models.TextField(default='Your Address Here')),
                ('card', models.IntegerField(default=0)),
                ('expiry', models.CharField(default='MM/YY', max_length=5)),
                ('cvv', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(choices=[('small', 'SMALL'), ('medium', 'MEDIUM'), ('large', 'LARGE')], default='medium', max_length=6)),
                ('crust', models.CharField(choices=[('normal', 'NORMAL'), ('thin', 'THIN'), ('thick', 'THICK'), ('gluten free', 'GLUTEN FREE')], default='normal', max_length=11)),
                ('sauce', models.CharField(choices=[('tomato', 'TOMATO'), ('bbq', 'BBQ')], default='tomato', max_length=6)),
                ('cheese', models.CharField(choices=[('small', 'SMALL'), ('medium', 'MEDIUM'), ('large', 'LARGE')], default='mozzarella', max_length=10)),
                ('pepperoni', models.BooleanField(default=False)),
                ('chicken', models.BooleanField(default=False)),
                ('ham', models.BooleanField(default=False)),
                ('pineapple', models.BooleanField(default=False)),
                ('pepper', models.BooleanField(default=False)),
                ('mushroom', models.BooleanField(default=False)),
                ('onion', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pizza')),
            ],
        ),
    ]
# Generated by Django 4.2.5 on 2023-09-14 22:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(6, 'El nombre de la categoria debe tener al menos 6 caracteres.')])),
            ],
        ),
        migrations.CreateModel(
            name='TypesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(6, 'El nombre de la transacción debe tener al menos 6 caracteres.')])),
            ],
        ),
    ]

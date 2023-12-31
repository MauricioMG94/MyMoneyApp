# Generated by Django 4.2.5 on 2023-09-14 22:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(6, 'El nombre debe tener al menos 6 caracteres.')], verbose_name='Nombre completo')),
                ('email', models.EmailField(max_length=100, unique=True, validators=[django.core.validators.EmailValidator('El correo proporcionado no es válido.'), django.core.validators.MinLengthValidator(6, 'El nombre debe tener al menos 6 caracteres.')], verbose_name='Correo electrónico')),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8, 'La contraseña debe tener al menos 8 caracteres.'), django.core.validators.MaxLengthValidator(12, 'La contraseña no puede tener más de 12 caracteres')], verbose_name='Contraseña')),
            ],
        ),
    ]

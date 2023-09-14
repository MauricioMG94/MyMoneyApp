from django.db import models
from django.core.validators import MinLengthValidator

class TypesModel(models.Model):
    id = models.AutoField(primary_key=True)
    transaction_name = models.CharField(max_length=20, validators=
                                 [MinLengthValidator(6, "El nombre de la transacción debe tener al menos 6 caracteres.")])

    
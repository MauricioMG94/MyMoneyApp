from django.db import models
from django.core.validators import MinLengthValidator
from apps.transactions.models.typesModel import TypesModel

class CategoriesModel(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20, validators=[
        MinLengthValidator(6, "El nombre de la categoria debe tener al menos 6 caracteres.")
    ])
    type = models.ForeignKey(TypesModel, on_delete=models.CASCADE, null=True, limit_choices_to={'transaction_name__isnull': False})

    def __str__(self):
        return self.category_name

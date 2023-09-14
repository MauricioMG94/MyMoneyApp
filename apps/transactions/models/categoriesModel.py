from django.db import models
from django.core.validators import MinLengthValidator

class CategoriesModel(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20, validators=
                                 [MinLengthValidator(6, "El nombre de la categoria debe tener al menos 6 caracteres.")])
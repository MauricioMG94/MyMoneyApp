from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from apps.users.models.userModel import UserModel
from apps.transactions.models.typesModel import TypesModel
from apps.transactions.models.categoriesModel import CategoriesModel

class ReportsModel(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    amount = models.FloatField(validators=[MinValueValidator(0.0, "La cantidad no puede ser negativa.")])
    information = models.CharField(
        max_length=100, 
        validators=[MinLengthValidator(6, "La información debe tener al menos 6 caracteres.")]
    )
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name="Usuario")
    type_id = models.ForeignKey(TypesModel, on_delete=models.CASCADE, verbose_name="Tipo")
    category_id = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE, verbose_name="Categoría")
    
    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
from django.contrib import admin
from apps.transactions.models.typesModel import TypesModel
from apps.transactions.models.categoriesModel import CategoriesModel

admin.site.register(TypesModel)
admin.site.register(CategoriesModel)


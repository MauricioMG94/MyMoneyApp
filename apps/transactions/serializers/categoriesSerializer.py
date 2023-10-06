from rest_framework import serializers
from apps.transactions.models.categoriesModel import CategoriesModel

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = ['id', 'category_name', 'type']
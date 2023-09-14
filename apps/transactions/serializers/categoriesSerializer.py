from rest_framework import serializers
from ..models.categoriesModel import CategoriesModel

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = ['id', 'category_name']
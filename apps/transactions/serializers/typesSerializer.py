from rest_framework import serializers
from ..models.typesModel import TypesModel

class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypesModel
        fields = ['id', 'transaction_name']
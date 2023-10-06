from rest_framework import serializers
from apps.transactions.models.typesModel import TypesModel

class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypesModel
        fields = ['id', 'transaction_name']
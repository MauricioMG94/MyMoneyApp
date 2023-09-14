from rest_framework import serializers
from ..models.reportModel import ReportsModel

class ReportsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportsModel
        fields = ['id', 'date', 'amount', 'information', 'user_id', 'type_id', 'category_id']


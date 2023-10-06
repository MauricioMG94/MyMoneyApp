from django.shortcuts import render

from rest_framework import viewsets
from apps.transactions.models.categoriesModel import CategoriesModel
from apps.transactions.models.typesModel import TypesModel
from apps.transactions.serializers.categoriesSerializer import CategoriesSerializer
from apps.transactions.serializers.typesSerializer import TypesSerializer


class CategoriesModelViewSet(viewsets.ModelViewSet):
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializer

class TypesModelViewSet(viewsets.ModelViewSet):
    queryset = TypesModel.objects.all()
    serializer_class = TypesSerializer


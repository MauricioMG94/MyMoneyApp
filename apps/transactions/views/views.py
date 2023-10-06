from django.shortcuts import render

from rest_framework import viewsets
from .models.categoriesModel import CategoriesModel
from .models.typesModel import TypesModel
from .serializers import CategoriesSerializer, TypesSerializer


class CategoriesModelViewSet(viewsets.ModelViewSet):
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializer

class TypesModelViewSet(viewsets.ModelViewSet):
    queryset = TypesModel.objects.all()
    serializer_class = TypesSerializer


from django.shortcuts import render

from rest_framework import viewsets
from .models.reportModel import ReportsModel
from .serializers import ReportsModelSerializer


class ReportsModelViewSet(viewsets.ModelViewSet):
    queryset = ReportsModel.objects.all()
    serializer_class = ReportsModelSerializer

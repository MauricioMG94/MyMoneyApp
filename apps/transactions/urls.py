from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.transactions.views.views import CategoriesModelViewSet, TypesModelViewSet
from . import views

router = DefaultRouter()
router.register('categorias', CategoriesModelViewSet)
router.register('tipos', TypesModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

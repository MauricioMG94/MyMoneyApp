from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', CategoriesModelViewSet)
router.register(r'types', TypesModelViewSet)

urlpatterns = [
    # Tus otras rutas aquí...
    path('api/', include(router.urls)),
]

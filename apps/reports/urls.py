from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'reports', ReportsModelViewSet)

urlpatterns = [
    # Tus otras rutas aquí...
    path('api/', include(router.urls)),
]

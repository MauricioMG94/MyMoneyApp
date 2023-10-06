from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # Tus otras rutas aquí
    path('api/', include(router.urls)),
]

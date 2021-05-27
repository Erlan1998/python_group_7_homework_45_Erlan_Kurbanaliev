from apiapp.views import ProductsViewSet, OrdersViewSet
from django.urls import include, path
from rest_framework import routers
router = routers.DefaultRouter()

router.register(r'products', ProductsViewSet)
router.register(r'orders', OrdersViewSet)
app_name = 'apiapp'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
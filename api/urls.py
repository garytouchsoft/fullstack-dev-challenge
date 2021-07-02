from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'shoesizes', views.ShoeSizeViewSet)
router.register(r'shoes', views.ShoeViewSet)
router.register(r'orders', views.OrderViewSet)


urlpatterns = [
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
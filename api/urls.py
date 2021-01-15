from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

router.register('product', views.ProductViewSet, basename='product')
router.register('client', views.ClientViewSet, basename='client')
router.register('order', views.OrderViewSet, basename='order')

urlpatterns = [
    path('', RedirectView.as_view(url="/admin/"), name='home'),
    path('', include(router.urls)),
]

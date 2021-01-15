from django.urls import path
from django.views.generic import RedirectView

from api import views

# home
urlpatterns = [
    path('', RedirectView.as_view(url="/admin/"), name='home'),
]

# product
urlpatterns += [
    path('product/', views.ProductAPIView.as_view(), name='product-list'),
    path('product/detail/<int:pk>/', views.ProductDetails.as_view(), name='product-detail'),
]

# client
urlpatterns += [
    path('client/', views.ClientAPIView.as_view(), name='client-list'),
    path('client/detail/<int:pk>/', views.ClientDetails.as_view(), name='client-detail'),
]

# order
urlpatterns += [
    path('order/', views.OrderAPIView.as_view(), name='order-list'),
    path('order/detail/<int:pk>/', views.OrderDetails.as_view(), name='order-detail'),
]

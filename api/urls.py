from django.urls import path
from django.views.generic import RedirectView

from api import views

# home
urlpatterns = [
    path('', RedirectView.as_view(url="/admin/"), name='home'),
]

# product
urlpatterns += [
    path('product/', views.product_list, name='product-list'),
    path('product/detail/<int:pk>/', views.product_detail, name='product-detail'),
]

# client
urlpatterns += [
    path('client/', views.client_list, name='client-list'),
    path('client/detail/<int:pk>/', views.client_detail, name='client-detail'),
]

# order
urlpatterns += [
    path('order/', views.order_list, name='order-list'),
    path('order/detail/<int:pk>/', views.order_detail, name='order-detail'),
]

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
    path('client_orders/<int:client_id>/<int:days>/', views.client_orders, name='client_orders'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('all_products/', views.all_products, name='all_products'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/', views.order_list, name='order_list'),
    path('order/create/', views.create_order, name='create_order'),
    path('order', views.order, name='order'),
    path('product', views.product, name='product'),
    path('client', views.client, name='client'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('remove_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('', views.cart_detail, name='cart_detail'),
]





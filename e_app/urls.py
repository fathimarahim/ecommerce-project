from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'e_app'

urlpatterns = [

    path('', views.allprodcat, name='allprodcat'),
    path('<slug:c_slug>/', views.allprodcat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.productdetail, name='product_details'),



]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

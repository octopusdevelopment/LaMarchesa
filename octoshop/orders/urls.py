from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [

path('create/', views.order_create, name='order_create'),
path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),
path('fetch/load-communes/', views.CommunesAPIView.as_view(), name='load_communes_fetch'),
path('fetch/load-wilaya/', views.load_wilaya_json, name='load_wilaya_fetch'),
path('api/load-commune/', views.CommunesAPIView.as_view(), name='load_wilaya_api')

]

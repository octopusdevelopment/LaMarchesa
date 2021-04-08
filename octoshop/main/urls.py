
from django.urls import path
from . import views
from .views import  IndexView, ContactFormView

app_name = 'main'
urlpatterns = [
    # path('produits/', ProductsView.as_view(), name='products'),
    path('about/', views.aboutView, name='about'),
    path('contact/', views.contactView, name='contact'),
    path('contact/send/', ContactFormView.as_view(), name= 'contact-send'),
    path('produits/<slug:slug>/<int:id>', views.productDetail, name='product-detail'),
    path('produits/', views.product_list, name='products'),
    path('produits/<slug:category_slug>/', views.product_list, name='prod-by-cat'),
    path('produits/<slug:category_slug>/', views.product_list, name='prod-by-sub-cat'),
    path('', views.IndexView.as_view(), name='index'),
]

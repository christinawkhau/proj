
from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:product_id>', views.product, name='product'),
    path('search', views.search, name='search'),
    #path('', views.categories, name='categories'),
    #path('categories/<int:category_id>/products/', views.products, name='products'),
    path('products/<int:category_id>/', views.products, name='products'),
]
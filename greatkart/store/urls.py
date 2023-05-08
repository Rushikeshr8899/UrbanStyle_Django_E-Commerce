from django.urls import path
from . import views

urlpatterns = [
   path('',views.store,name="store"),
   # path('<slug:category_slug>/', views.store, name='products_by_category'),
   path('<slug:category_name>/',views.store,name="category_product"),
   path('<slug:category_name>/<slug:product_name>/', views.product_detail, name='product_detail'),

]

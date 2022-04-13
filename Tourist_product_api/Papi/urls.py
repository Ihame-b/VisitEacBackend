from django import views
from django.urls import path
from . import views

urlpatterns = [
   #path('', views.apiOverview, name='apiOverview'),#viewproduct, deleteproduct , viewproduct
   path('product-list/', views.ShowAll, name='product-list'),
   path('product-detail/<int:pk>/', views.viewproduct, name='product-detail'),
   # path('product-create/', views.Createproduct, name='product-create'),
    path('productv', views.productview, name='productv'),
   path('product-update/<int:pk>/', views.Updateproduct, name='product-update'),
   path('product-delete/<int:pk>/', views.deleteproduct, name='product-delete'),
   path('create/', views.ProductCreateView.as_view(), name='create'),
   path('create-product', views.create_Peoduct_View, name="create_product")
] 

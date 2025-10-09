from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
  path('', ProductListView.as_view(), name='product-list'),
  path("create/", ProductCreateView.as_view(), name="create-product"),
  path('<int:pk>', ProductDetailView.as_view(), name='product-detail'),
  path('<int:pk>/update', ProductUpdateView.as_view(), name='update-product'),
  path('<int:pk>/delete', ProductDeleteView.as_view(), name='delete-product'),
  
]

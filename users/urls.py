from django.urls import path, include
from .views import RegisterView, LoginView, index

urlpatterns = [
  path( '', index, name='index'),
  path('register/', RegisterView.as_view(), name = 'register'),
  path('login/', LoginView.as_view(), name='views'),
  path('products/', include('products.urls'))
]
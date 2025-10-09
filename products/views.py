from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAdminUser
from .models import Product
from .serializers import ProdcutSerializer
from django.http import HttpResponse

# Create your views here.

# - GET /products: Get a list of products (public).  
class ProductListView(APIView):
  permission_classes = [AllowAny]
  
  def get(sef, request):
    products = Product.objects.all()
    serializer = ProdcutSerializer(products, many=True)
    return Response(serializer.data)
    
# POST /products: Add a new product (Admin only).
class ProductCreateView(APIView):
  permission_classes = [IsAuthenticated, IsAdminUser]
  def post(self, request):
    serializer = ProdcutSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
# - GET /products/:id: Get a specific product by ID (public).
class ProductDetailView(APIView):
  permission_classes = [AllowAny]
  
  def get(self, request, pk):
    try:
      product = Product.objects.get(pk=pk)
      serializer = ProdcutSerializer(product)
      return Response(serializer.data)
    except Product.DoesNotExist:
      return Response('Product not found', status=status.HTTP_404_NOT_FOUND)
    
# - PUT /products/:id: Update product details (Admin only).
class ProductUpdateView(APIView):
  permission_classes = [IsAuthenticated, IsAdminUser]
  def put(self, request, pk):
    try:
      product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
      return Response({'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProdcutSerializer(product, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# - DELETE /products/:id: Delete a product (Admin only).
class ProductDeleteView(APIView):
  permission_classes = [IsAuthenticated, IsAdminUser]
  def delete(self, request, pk):
    try:
      product = Product.objects.get(pk=pk)
      product.delete()
      return Response({'Product deleted'}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
      return Response({'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    

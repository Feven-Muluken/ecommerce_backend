from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
# POST /auth/register:'sabe'
# POST /auth/login:'lkjkj'
def index(request):
  return HttpResponse("Hello world welcome to ecomerce website")

class RegisterView(APIView):
  def post(self, request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
  
class LoginView(APIView):
  def post(self, request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.validated_data
      refresh = RefreshToken.for_user(user)
      return Response({
        'access' : str(refresh.access_token),
        'refresh': str(refresh)
      }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

   # for regiter testing purpose
# {
#   "username": "feven123",
#   "email": "feven@example.com",
#   "password": "securePassword123",
#   "role": "user"
# }
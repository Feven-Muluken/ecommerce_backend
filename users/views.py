from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegisterSerializer
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
      return Response({"message": "User regitered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


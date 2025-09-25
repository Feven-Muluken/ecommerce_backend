from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = '[__all__]'
      extra_kwargs = {
        'password': {'write_only': True}
      }
  def create(self, validated_data):
    validated_data['password'] = make_password(validated_data['password'])
    
    return User.objects.create(**validated_data)
        
class LoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email', 'password']
    extra_kwargs = {
      'password': {'write_only': True}
    }
    
    # Example usage:
# instance = User.objects.get(pk=1)
# serializer = RegisterSerializer(instance)
# print(serializer.data) # This will be a dictionary, ready to be converted to JSON
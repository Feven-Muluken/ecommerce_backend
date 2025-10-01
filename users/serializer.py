from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password

User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = '__all__'
      extra_kwargs = {
        'password': {'write_only': True}
      }
  def create(self, validated_data):
    validated_data['password'] = make_password(validated_data['password'])
    
    return User.objects.create(**validated_data)
        
class LoginSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField(write_only=True)

  def validate(self, data):
    user = authenticate(email=data['email'], password=data['password']) 
    if not user:
      raise serializers.ValidationError("Invalid email or password")
    return user
    
    # Example usage:
# instance = User.objects.get(pk=1)
# serializer = RegisterSerializer(instance)
# print(serializer.data) # This will be a dictionary, ready to be converted to JSON
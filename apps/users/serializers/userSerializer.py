from rest_framework import serializers
from ..models.userModel import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'full_name', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
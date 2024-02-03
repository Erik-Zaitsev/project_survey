from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'date_joined',
            'last_login',
            'is_staff',
            'is_superuser',
            'is_active',
        ]
        
    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)
    
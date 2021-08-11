from django.db.models import fields
from rest_framework import serializers


from .models import User



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ("email", "password")
    
    def create(self, validated_data):
        user = User.objects.create_user(email = validated_data["email"], password = validated_data["password"])
        return user
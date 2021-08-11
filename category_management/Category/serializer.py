from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from Category.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)
    def to_representation(self, instance):
        data = super(CategorySerializer,self).to_representation(instance)
        data["id"] = instance.id
        return data
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name",instance.name)
        instance.save()
        return instance
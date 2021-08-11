from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from Product.models import Product,ProductTags,Tags
import json


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = ("name",)

class ProductTagsSerializer(ModelSerializer):
    tags_id = TagSerializer()
    class Meta:
        model = ProductTags
        fields = ("product_id","tags_id")
    def to_representation(self, instance):
        data = super(ProductTagsSerializer ,self).to_representation(instance)
        print(data["tags_id"]["name"])

        return {"name":data["tags_id"]["name"]}

class GetProductListSerializer(ModelSerializer):
    products = ProductTagsSerializer(many=True)
    class Meta:
        model = Product
        fields = ("products",)
    
    def to_representation(self, instance):
        data = super(GetProductListSerializer ,self).to_representation(instance)
        context = {
            "name":instance.name,
            "image":instance.image.url,
            "desc":instance.desc,
            "category_id":instance.category_id.name,
            "tags":data["products"]
        }
        return context



class ProductSerializer(ModelSerializer):
    tags = serializers.CharField()
    class Meta:
        model = Product
        fields = ("name","category_id","image", "desc", "tags")
    
    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        data["id"] = instance.id
        return data
    
    def update(self, instance, validated_data):
        tags = str(json.loads(validated_data["tags"])).split(",")
        instance.name = validated_data.get("name",instance.name)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.image = validated_data.get("image", instance.image)
        instance.desc = validated_data.get("desc", instance.desc)
        instance.save()
        ProductTags.objects.filter(product_id = instance.id).delete()
        for x in tags:
          
            try:
                tags_instance = Tags.objects.get(name=x)
            except Tags.DoesNotExist:
                tags_instance = Tags.objects.create(name=x)
            ProductTags.objects.get_or_create(tags_id=tags_instance, product_id=instance) 

            

        return instance
       
    
    
    def create(self, validated_data):
        saving_tags = str(validated_data["tags"]).split(",")
        del validated_data["tags"]
        product = Product.objects.create(**validated_data)
        for x in saving_tags:
            try:
                tags_instance = Tags.objects.get(name=x)
            except Tags.DoesNotExist:
                tags_instance = Tags.objects.create(name=x)
            ProductTags.objects.get_or_create(tags_id=tags_instance, product_id=product)         
        
        return product
    
   

        
    
 
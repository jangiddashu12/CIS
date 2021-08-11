import re
from django.db.models.fields import files
from django.shortcuts import render
from rest_framework import serializers

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from Product.serializer import ProductSerializer,GetProductListSerializer
from rest_framework.response import Response
from rest_framework import status
from Product.models import Product
import json


class ProductCreateView(APIView):

    def get(self, request):
        try:
            products = Product.objects.all()
            serializer = GetProductListSerializer(instance=products, many=True)
            return Response({"data":serializer.data, "message":"fetched Succefully", "error":0}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"data":[], "message":str(e), "error":1}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

 
    def post(self,request):
        try:
            print("data", request.data)
            exist_products = Product.objects.filter(name=request.data["name"])
            if exist_products.count()>0:
                return Response({"data":[], "message":"this product is already exists", "error":1}, status=status.HTTP_400_BAD_REQUEST)

            serializer = ProductSerializer(data=request.data)
        
            if serializer.is_valid():
                serializer.save()
                
                return Response({"data":[], "message":"Saved Succefully", "error":0}, status=status.HTTP_200_OK)
            else:
                # print("serializer.error_messages",serializer.errors)
                return Response({"data":[], "message":serializer.errors["name"][0], "error":1}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"data":[], "message":str(e), "error":1}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def put(self, request):
        try:
            product_instance = Product.objects.get(id = int(request.data["id"]))
            del request.data["id"]
            data = request.data
            
            serializer = ProductSerializer(instance = product_instance,data=data)
            print("serializer.is_valid()",serializer.is_valid())
            if serializer.is_valid(raise_exception=True):
                # print("data========>>>>>>>>>>>", serializer.validated_data)
                serializer.update(instance=product_instance,validated_data=serializer.validated_data)
                # print(json.dumps(serializer.errors))
                return Response({"data":"update successfully", "message":"Saved Succefully", "error":0}, status=status.HTTP_200_OK)
            else:
                return Response({"data":[], "message":"serializer.errors", "error":1}, status=status.HTTP_400_BAD_REQUEST)
            
        except Product.DoesNotExist or Product.MultipleObjectsReturned:
                return Response({"data":[], "message":"Please send valid data", "error":1}, status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:
            print(e)
            return Response({"data":[], "message":str(e), "error":1}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:

            Product.objects.filter(id = request.data["id"]).delete()
            return Response({"data":[], "message":"Deleted Succefully", "error":0}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"data":[], "message":str(e), "error":1}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

            






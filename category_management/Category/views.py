from Category.models import Category
from django.shortcuts import render
from rest_framework.views import APIView
from Category.models import Category
from Category.serializer import CategorySerializer
from rest_framework.response import Response
from rest_framework import serializers, status
# Create your views here.

class CategoryView(APIView):
    def get(self,request):
        category_instance = Category.objects.all()
        serialzier = CategorySerializer(category_instance, many=True)
        return Response({"data":serialzier.data,"message":"data", "error":0},status=status.HTTP_200_OK)
    
    def post(self,request):
        try:
            serializer = CategorySerializer(data=request.data, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"data":[], "message":"Saved Succefully", "error":0}, status=status.HTTP_200_OK)
            else:
                return Response({"data":[], "message":serializer.errors["name"][0], "error":0}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data":[], "message":str(e), "error":1}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self,request):
        try:
            instance_cat = Category.objects.get(id = request.data["id"])
            serializer = CategorySerializer(instance=instance_cat,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.update(instance=instance_cat, validated_data=serializer.validated_data)
                return Response({"data":[], "message":"Update Succefully", "error":0}, status=status.HTTP_200_OK)
            else:
                return Response({"data":[], "message":serializer.errors["name"][0], "error":0}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data":[], "message":str(e), "error":1}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            





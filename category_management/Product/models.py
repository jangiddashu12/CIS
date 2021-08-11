from Category.models import Category
from django.db import models
from Category.models import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255,)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/%Y/%m/%d/', null=True, max_length=255)
    desc = models.TextField(max_length=1000)


class Tags(models.Model):
    name = models.CharField(max_length=255)


class ProductTags(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    tags_id = models.ForeignKey(Tags, on_delete=models.CASCADE)

    
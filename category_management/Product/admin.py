from Product.models import Product
from django.contrib import admin
from Product.models import Product,Tags
# Register your models here.

admin.site.register(Tags)

class ProductAdmin(admin.ModelAdmin):
    list_display=("name","image","category_id","desc")
    search_fields = ['name',  ]
admin.site.register(Product,ProductAdmin)
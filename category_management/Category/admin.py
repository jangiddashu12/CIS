from django.contrib import admin
from Category.models import Category
# Register your models here.



class CatAdmin(admin.ModelAdmin):
    list_display=("name",)
    search_fields = ['name',  ]
admin.site.register(Category,CatAdmin)
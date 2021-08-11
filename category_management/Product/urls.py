
from django.urls import path
from Product.views import ProductCreateView
urlpatterns = [
 path("add-product",ProductCreateView.as_view() )  ,
 path("update-product",ProductCreateView.as_view(), )  ,
 path("get-products",ProductCreateView.as_view())
]

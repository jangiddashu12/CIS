
from django.urls import path
from Category.views import CategoryView
urlpatterns = [
   path("get-category", CategoryView.as_view()),
   path("add-category", CategoryView.as_view()),
   path("update-category", CategoryView.as_view()),
]

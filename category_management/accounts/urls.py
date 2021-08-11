from django.urls import path

from .views import UserSignup,Userlogin

urlpatterns = [
   path("signup", UserSignup.as_view()),
   path("login", Userlogin.as_view())
]
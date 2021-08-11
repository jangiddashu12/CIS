
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import User

from accounts.serializers import UserSerializer


class UserSignup(APIView):
        def post(self, request):
            # try:
            data = request.data
            user = User.objects.filter(email = data['email'])
            if user:
                context = {
                    "data" : "" ,
                    'message'   : "Email Already Used"
                }
                return Response(context, status= status.HTTP_200_OK)
            else:
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    user = User.objects.get(email = data['email'])
                    token = Token.objects.create(user=user)
                    context = {
                        "data" : str(token),
                        'message': "Signup Succesfull"
                    }
                    return Response(context, status.HTTP_200_OK)
                else:
                    context = {
                        'data': serializer.error,
                        "message":"Error"
                    }
                    return Response(context, status.HTTP_200_OK)
            # except Exception as e:
            #         context = {
            #                     "error": str(e),
            #                     'message':'Error Occured'
            #                 }
            #         return Response(context,status=status.HTTP_400_BAD_REQUEST)

class Userlogin(APIView):
    def post(self, request):
        try:
            data = request.data
            user = User.objects.filter(email = data['email'], active = True).first()
            if user:
                print(data["password"])
                if user.check_password(data["password"]):
                    token = Token.objects.filter(user = user).first()
                    if token:
                        token.delete()
                    token = Token.objects.update_or_create(user = user)
                    context = {
                        'data': str(token[0]),
                        'message': "Login Sucessfull"
                    }
                    return Response(context, status.HTTP_200_OK) 
                else:
                    context = {
                        'data': "",
                        'message' :"Enter Password correctly"
                    }
                    return Response(context, status.HTTP_200_OK)
            else:
                context = {
                        'data':"" ,
                        'message': "Enter Valid Email"
                    }
                return Response(context, status.HTTP_200_OK)
        except Exception as e:
            context = {
                        "error": str(e),
                        'message':'Error Occured'
                    }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

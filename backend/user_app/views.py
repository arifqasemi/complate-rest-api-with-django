from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from user_app.serializer import RegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(['GET', 'POST'])
def RegisterView(request):
    if request.method == "GET":
        # Handle GET request logic here if needed
        return Response({"message": "GET request handled"})

    if request.method == "POST":
        serialized_user = RegisterSerializer(data=request.data)
        data = {}
        if serialized_user.is_valid():
           account =  serialized_user.save()
           token = Token.objects.get(user=account).key
           data['email'] = account.email
           data['username'] = account.username
           data['token'] = token
           return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)


def LogoutView(request):
    if request.method == "POST":
        request.user.auth_token.delete()    
        return Response(status=status.HTTP_404_NOT_FOUND)
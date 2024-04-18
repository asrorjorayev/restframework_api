from django.shortcuts import render
from .serializers import *
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
class UsersvIew(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        users=User.objects.all()
        serializer=UserSerializerView(users,many=True)
        return Response(data=serializer.data)
class UserView(APIView):
    def get(self,request,id):
        user=User.objects.get(id=id)
        serializer=UserSerializerView(user)
        return Response(serializer.data)
    
    def put(self,request,id):
        user=User.objects.get(id=id)
        serializer=UserSerializerView(user,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        


    

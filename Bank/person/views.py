from django.shortcuts import render,get_list_or_404
from rest_framework.views import APIView
from .serializers import*
from rest_framework.response import Response
from .models import Student
from rest_framework.permissions import IsAuthenticated
class PersonsView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        person=Student.objects.all()
        serializer=PersonSerializerView(person,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=PersonSerializerView(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

class PersonUpdateView(APIView):
    def put(self,request,id):
        person=Student.objects.get(id=id)
        serializer=PersonSerializerView(instance=person,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id):
        
        try:
            person=Student.objects.get(id=id)

        except Student.DoesNotExist:
            return Response({"messege":"Bunday model Mavjud emas"})
        person.delete()
        return Response({"messege":"Muvaffaqiyatli o'chirildi"})
    


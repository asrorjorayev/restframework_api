from rest_framework import serializers
from .models import User


class UserSerializerView(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','first_name','last_name','email','phone_number','image']
        

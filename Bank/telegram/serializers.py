from rest_framework import serializers
from api.models import User



class RegisterTgSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','phone_number']


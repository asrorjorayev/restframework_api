from django.shortcuts import render
from .serializers import RegisterTgSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from telegram.ext import Updater, CommandHandler
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import User
from django.contrib.auth import authenticate

 
def start(update, context):
    update.message.reply_text(" Botimizga xush kelibsiz!")

 
def initialize_telegram_bot(refresh):
    TOKEN = str(refresh.access_token)
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

class TgRegisterView(APIView):
    def post(self, request):
        serializer = RegisterTgSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.data['phone_number'])
        refresh = RefreshToken.for_user(user)
      
        initialize_telegram_bot(refresh)
        
        return Response({'message': 'User registered successfully'})

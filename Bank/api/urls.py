from django.urls import path
from .views import UsersvIew,UserView

app_name='user'
urlpatterns=[
    path('users_page/',UsersvIew.as_view(),name='users_view'),
    path('user_page/<int:id>/',UserView.as_view(),name='user_view'),
   
]
from django.urls import path
from .views import TgRegisterView

app_name='telegram'

urlpatterns={
    path('telegram/',TgRegisterView.as_view(),name="telegram")
}
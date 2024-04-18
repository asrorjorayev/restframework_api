from django.urls import path
from .views import *

app_name='person'
urlpatterns=[
    path('persons/',PersonsView.as_view(),name='persons'),
    path('persons-update/<int:id>/',PersonUpdateView.as_view(),name='person_update'),
 
]
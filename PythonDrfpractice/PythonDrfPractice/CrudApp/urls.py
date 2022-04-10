from django.contrib import admin
from django.urls import path
# from .serializer import *
# from models import *
from .views import *

urlpatterns = [
    path('Register/', Register.as_view()),
    path('Update/<int:id>', Update.as_view()),
    path("GetDetails/",GetDetails.as_view()),
    path('Delete/<int:id>/',Delete.as_view())
]

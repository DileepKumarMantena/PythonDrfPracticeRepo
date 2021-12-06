from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('Registration', Registration.as_view()),
    path('Retrive',Retrive.as_view()),
    path('Update/<int:id>/',Update.as_view())

]

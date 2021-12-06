from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('Registration', MemberPost.as_view()),
    path("Membe/<int:id>/", Member.as_view())

]

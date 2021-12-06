from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .models import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView

from .serializers import *


class MemberPost(CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = Memberserializer


class Member(RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = Memberserializer

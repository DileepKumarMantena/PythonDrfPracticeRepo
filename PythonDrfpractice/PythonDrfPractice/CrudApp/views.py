from django.shortcuts import render

# Create your views here.
from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import JSONRenderer

from .models import *
from .serializer import RegisterSerializer
from rest_framework import generics, status, request
from rest_framework.response import Response
from .serializer import RegisterSerializer
from rest_framework import serializers


class Register(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                counter=0
                user = serializer.save()
                counter1=counter+1
                print(counter1)
            return Response({
                "Message": "Successfull",
                "Result": serializer.data
            })
        except Exception as e:
            return Response({
                "Message": "Fail",
                "Result": []
            })


class Update(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def put(self, request, id):
        try:
            r = RegistrationModel.objects.get(id=id)

            s = RegisterSerializer(r, data=request.data)
            s.is_valid(raise_exception=True)
            s.save()

            return Response({
                'message': 'Successful',
                "Result": s.data,
                'HasError': False,
                'status': 200
            })
        except RegistrationModel.DoesNotExist as e:

            return Response({
                'message': 'Fail',
                'HasError ': True,
                'status': 400
            })


class GetDetails(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            queryset = RegistrationModel.objects.all()
            serializer_class = RegisterSerializer(queryset, many=True)
            return Response({
                'message': 'Successful',
                'Result': serializer_class.data,
                'HasError': False,
                'status': 200
            })
        except Exception as e:
            return Response({
                'message': 'Fail',
                'Result': [],
                'HasError': True,
                'status': 400
            })


class Delete(generics.GenericAPIView):
    def delete(self, request, id):
        counter=0
        d = RegistrationModel.objects.get(id=id)
        d.delete()
        counter2=counter-1
        print(counter2)
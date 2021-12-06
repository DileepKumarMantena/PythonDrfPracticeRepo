from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .serializers import *


class Registration(generics.GenericAPIView):
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'message': 'Successful',
            'Result': StudentSerializer(user).data,
            'HasError': False,
            'status': 200

        })


class Retrive(APIView):
    serializer_class = GetStudentSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request):
        queryset = Student.objects.all()
        serializer_class = GetStudentSerializer(queryset, many=True)
        serializer_class.is_valid(raise_exception=True)
        user = serializer_class.save()
        return Response({
            'message': 'Successful',
            'Result': GetStudentSerializer(user).data,
            'HasError': False,
            'status': 200

        })


class Update(generics.GenericAPIView):
    serializer_class = StudentSerializer

    def put(self, request, id):
        try:
            r = StudentSerializer.objects.get(id=id)
            first_name = request.data.get("Address")
            last_name = request.data.get("Country")
            grade = request.data.get("State")
            age = request.data.get("City")

            data = {'first_name': first_name, 'last_name': last_name, 'grade': grade, 'age': age}
            s = StudentSerializer(r, data=data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            return Response({'message': ' Successful',
                             'Result': True,
                             'HasError': False,
                             'status': 200
                             })
        except Student.DoesNotExist:
            return Response({'message': 'not updated',
                             'Result': False,
                             'HasError': True,
                             'status': 400
                             })

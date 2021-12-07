from rest_framework import generics, viewsets
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from .serializers import *


class Bmi(generics.GenericAPIView):
    serializer_class = ConverterSerializer

    def post(self, request, *args, **kwargs):
        form = ConverterSerializer(data=request.data)
        print(form)
        form.is_valid()
        user = form.save()
        return Response(DataSerializer(user).data)


class Get(generics.GenericAPIView):
    serializer_class = DataSerializer

    def get(self, request):
        a = Bodymass.objects.all()
        serializer = DataSerializer(a, many=True)
        print(serializer.data)
        return Response(serializer.data)


class GetById(generics.GenericAPIView):
    serializer_class = DataSerializer

    def get(self, request, id):
        a = Bodymass.objects.get(id=id)
        serializer_class = DataSerializer(a)
        return Response(serializer_class.data)


class Delete(generics.GenericAPIView):
    serializer_class = ConverterSerializer

    def delete(self, request, id):
        c = Bodymass.objects.get(id=id)
        c.delete()
        return Response(c)


class Update(UpdateAPIView):
    serializer_class = ConverterSerializer
    queryset = Bodymass.objects.all()

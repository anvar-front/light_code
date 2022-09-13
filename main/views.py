from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class EmployeeAPIView(APIView):

    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class MachineAPIView(APIView):

    def get(self, request, format=None):
        machine = Machine.objects.all()
        serializer = MachineSerializer(machine, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class WorkAPIView(APIView):

    def get(self, request, format=None):
        work = Work.objects.all()
        serializer = WorkSerializer(work, many=True)
        return Response(serializer.data)
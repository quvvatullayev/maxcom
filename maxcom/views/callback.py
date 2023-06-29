from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from ..models import (
    CallBack,
)
from ..serializers import (
    CallBackSerializer,
)

class CallBackCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Create new callback",
        request_body=CallBackSerializer,
        responses={
            201: CallBackSerializer,
            400: "Bad request",
        }
    )
    def post(self, request: Request):
        data = request.data
        serializer = CallBackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)
    
class CallBackDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete callback",
        responses={
            200: "OK",
            400: "Bad request",
        }
    )
    def delete(self, request: Request, pk: int):
        callback = CallBack.objects.get(id=pk)
        if callback:
            callback.delete()
            return Response({"message": "Deleted"}, status=status.HTTP_200_OK)
        return Response({"message": "Not found"}, status=status.HTTP_400_BAD_REQUEST)
    
class CallBackListView(APIView):
    @swagger_auto_schema(
        operation_description="Get all callbacks",
        responses={
            200: CallBackSerializer(many=True),
            400: "Bad request",
        }
    )
    def get(self, request: Request):
        callbacks = CallBack.objects.all()
        serializer = CallBackSerializer(callbacks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CallBackDetailView(APIView):
    @swagger_auto_schema(
        operation_description="Get callback by id",
        responses={
            200: CallBackSerializer,
            400: "Bad request",
        }
    )
    def get(self, request: Request, pk: int):
        callback = CallBack.objects.get(id=pk)
        serializer = CallBackSerializer(callback)
        return Response(serializer.data, status=status.HTTP_200_OK)




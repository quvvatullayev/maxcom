from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    About,
)
from ..serializers import (
    AboutSerializer,
)

class AboutCreateView(APIView):
    @swagger_auto_schema(
        request_body=AboutSerializer,
        operation_description="Create new about",
        operation_summary="Create new about",
        responses={
            201: AboutSerializer,
            400: "Bad request"
        }
    )
    def post(self, request:Request):
        data = request.data
        serializer = AboutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)
    
class AboutUpdateView(APIView):
    @swagger_auto_schema(
        request_body=AboutSerializer,
        operation_description="Update about",
        operation_summary="Update about",
        responses={
            200: AboutSerializer,
            400: "Bad request"
        }
    )
    def put(self, request:Request, pk:int):
        about = About.objects.get(pk=pk)
        about.title = request.data['title']
        about.description = request.data['description']
        about.save()
        serializer = AboutSerializer(about)
        return Response(serializer.data, status=status.HTTP_200_OK,)
    
class AboutGetView(APIView):
    @swagger_auto_schema(
        operation_description="Get about",
        operation_summary="Get about",
        responses={
            200: AboutSerializer,
            400: "Bad request"
        }
    )
    def get(self, request:Request):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK,)
    
class AboutGetIdView(APIView):
    @swagger_auto_schema(
        operation_description="Get about by id",
        operation_summary="Get about by id",
        responses={
            200: AboutSerializer,
            400: "Bad request"
        }
    )
    def get(self, request:Request, pk:int):
        about = About.objects.get(pk=pk)
        serializer = AboutSerializer(about)
        return Response(serializer.data, status=status.HTTP_200_OK,)
    
class AboutDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete about",
        operation_summary="Delete about",
        responses={
            204: "No content",
            400: "Bad request"
        }
    )
    def delete(self, request:Request, pk:int):
        about = About.objects.get(pk=pk)
        about.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Category,
)

from ..serializers import (
    CategorySerializer,
)

class CategoryCreateView(APIView):
    @swagger_auto_schema(
        request_body=CategorySerializer,
        operation_description="Create new category",
        operation_summary="Create new category",
        responses={
            201: CategorySerializer,
            400: "Bad request"
        }
    )
    def post(self, request: Request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryUpdateView(APIView):
    @swagger_auto_schema(
        request_body=CategorySerializer,
        operation_description="Update category",
        operation_summary="Update category",
        responses={
            200: CategorySerializer,
            400: "Bad request"
        }
    )
    def put(self, request: Request, pk: int):
        category = Category.objects.get(pk=pk)
        category.name = request.data['name']
        category.description = request.data['description']
        category.save()
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete category",
        operation_summary="Delete category",
        responses={
            204: "No content",
            400: "Bad request"
        }
    )
    def delete(self, request: Request, pk: int):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CategoryGetView(APIView):
    # get all categories
    @swagger_auto_schema(
        operation_description="Get all categories",
        operation_summary="Get all categories",
        responses={
            200: CategorySerializer,
            400: "Bad request"
        }
    )
    def get(self, request: Request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CategoryGetIdView(APIView):
    # get category by id
    @swagger_auto_schema(
        operation_description="Get category by id",
        operation_summary="Get category by id",
        responses={
            200: CategorySerializer,
            400: "Bad request"
        }
    )
    def get(self, request: Request, pk: int):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
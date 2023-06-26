from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    SubCategory,
)

from ..serializers import (
    SubCategorySerializer,
    CreateSubCategorySerializer,
)

class SubCategoryCreateView(APIView):
    @swagger_auto_schema(
        request_body=CreateSubCategorySerializer,
        operation_description="Create new subcategory",
        operation_summary="Create new subcategory",
        responses={
            201: SubCategorySerializer,
            400: "Bad request"
        }
    )
    def post(self, request: Request):
        serializer = CreateSubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubCategoryUpdateView(APIView):
    @swagger_auto_schema(
        request_body=SubCategorySerializer,
        operation_description="Update subcategory",
        operation_summary="Update subcategory",
        responses={
            200: SubCategorySerializer,
            400: "Bad request"
        }
    )
    def put(self, request: Request, pk: int):
        subcategory = SubCategory.objects.get(pk=pk)
        subcategory.name = request.data['name']
        subcategory.description = request.data['description']
        subcategory.save()
        serializer = SubCategorySerializer(subcategory)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SubCategoryDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete subcategory",
        operation_summary="Delete subcategory",
        responses={
            204: "No content",
            400: "Bad request"
        }
    )
    def delete(self, request: Request, pk: int):
        subcategory = SubCategory.objects.get(pk=pk)
        subcategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SubCategoryGetIdView(APIView):
    @swagger_auto_schema(
        operation_description="Get subcategory by id",
        operation_summary="Get subcategory by id",
        responses={
            200: SubCategorySerializer,
            400: "Bad request"
        }
    )
    def get(self, request: Request, pk: int):
        subcategory = SubCategory.objects.get(pk=pk)
        serializer = SubCategorySerializer(subcategory)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SubCategoryGetView(APIView):
    @swagger_auto_schema(
        operation_description="Get all subcategories",
        operation_summary="Get all subcategories",
        responses={
            200: SubCategorySerializer,
            400: "Bad request"
        }
    )
    def get(self, request: Request):
        subcategory = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategory, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
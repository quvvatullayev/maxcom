from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    ProductImage,
)
from ..serializers import (
    ProductImageSerializer,
    CreateProductImageSerializer,
)

class ProductImageCreateView(APIView):
    @swagger_auto_schema(
        request_body=CreateProductImageSerializer,
        operation_description="Create new product image",
        operation_summary="Create new product image",
        responses={
            201: ProductImageSerializer,
            400: "Bad request"
        }
    )
    def post(self, request: Request):
        serializer = CreateProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductImageUpdateView(APIView):
    @swagger_auto_schema(
        request_body=ProductImageSerializer,
        operation_description="Update product image",
        operation_summary="Update product image",
        responses={
            200: ProductImageSerializer,
            400: "Bad request"
        }
    )
    def put(self, request: Request, pk: int):
        productimage = ProductImage.objects.get(pk=pk)
        productimage.image = request.data['image']
        productimage.save()
        serializer = ProductImageSerializer(productimage)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProductImageDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete product image",
        operation_summary="Delete product image",
        responses={
            200: "OK",
            400: "Bad request"
        }
    )
    def delete(self, request: Request, pk: int):
        productimage = ProductImage.objects.get(pk=pk)
        productimage.delete()
        return Response(status=status.HTTP_200_OK)
    
class ProductImageGetIdView(APIView):
    @swagger_auto_schema(
        operation_description="Get product image by id",
        operation_summary="Get product image by id",
        responses={
            200: ProductImageSerializer,
            400: "Bad request"
        }
    )
    def get(self, request: Request, pk: int):
        productimage = ProductImage.objects.get(pk=pk)
        serializer = ProductImageSerializer(productimage)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProductImageGetView(APIView):
    @swagger_auto_schema(
        operation_description="Get all product images",
        operation_summary="Get all product images",
        responses={
            200: ProductImageSerializer,
            400: "Bad request"
        }
    )
    def get(self, request: Request):
        productimages = ProductImage.objects.all()
        serializer = ProductImageSerializer(productimages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
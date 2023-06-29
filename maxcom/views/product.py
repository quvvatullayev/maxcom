from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Product,
    ProductImage,
)
from ..serializers import (
    ProductSerializer,
    CreateProductSerializer,
    ProductImageSerializer,
)

class ProductCreateView(APIView):
    @swagger_auto_schema(
        request_body=CreateProductSerializer,
        operation_description="Create new product",
        operation_summary="Create new product",
        responses={
            201: ProductSerializer,
            400: "Bad request"
        }
    )
    def post(self, request: Request):
        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductUpdateView(APIView):
    @swagger_auto_schema(
        request_body=ProductSerializer,
        operation_description="Update product",
        operation_summary="Update product",
        responses={
            200: ProductSerializer,
            400: "Bad request"
        }
    )
    def put(self, request: Request, pk: int):
        product = Product.objects.get(pk=pk)
        product.name = request.data['name']
        product.brand = request.data['brand']
        product.description = request.data['description']
        product.price = request.data['price']
        product.discount = request.data['discount']
        product.image = request.data['image']
        product.short_description = request.data['short_description']
        product.live = request.data['live']
        product.likes = request.data['likes']
        product.status = request.data['status']
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProductDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete product",
        operation_summary="Delete product",
        responses={
            204: "No content",
            400: "Bad request"
        }
    )
    def delete(self, request: Request, pk: int):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ProductGetIdView(APIView):
    @swagger_auto_schema(
        operation_description="Get product by id",
        operation_summary="Get product by id",
        responses={
            200: ProductSerializer,
            400: "Bad request"
        }
    )
    def get(self, request: Request, pk: int):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        product_image = ProductImage.objects.filter(product=product)
        serializer_image = ProductImageSerializer(product_image, many=True)
        data = {
            'product': serializer.data,
            'product_image': serializer_image.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
class ProductGetView(APIView):
    @swagger_auto_schema(
        operation_description="Get all products",
        operation_summary="Get all products",
        responses={
            200: ProductSerializer,
            400: "Bad request"
        }
    )
    def get(self, request: Request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
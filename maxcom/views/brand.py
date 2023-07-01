from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Brand,
)
from ..serializers import (
    BrandSerializer,
)

class BrandCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Create new brand",
        request_body=BrandSerializer,
        responses={
            201: BrandSerializer,
            400: "Bad request",
        }
    )
    def post(self, request: Request):
        data = request.data
        serializer = BrandSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)
    
class BrandDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete brand",
        responses={
            200: "OK",
            400: "Bad request",
        }
    )
    def delete(self, request: Request, pk: int):
        brand = Brand.objects.get(id=pk)
        if brand:
            brand.delete()
            return Response({"message": "Deleted"}, status=status.HTTP_200_OK)
        return Response({"message": "Not found"}, status=status.HTTP_400_BAD_REQUEST)
    
class BrandListView(APIView):
    @swagger_auto_schema(
        operation_description="Get all brands",
        responses={
            200: BrandSerializer(many=True),
            400: "Bad request",
        }
    )
    def get(self, request: Request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BrandDetailView(APIView):
    @swagger_auto_schema(
        operation_description="Get brand by id",
        responses={
            200: BrandSerializer,
            400: "Bad request",
        }
    )
    def get(self, request: Request, pk: int):
        brand = Brand.objects.get(id=pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BrandUpdateView(APIView):
    @swagger_auto_schema(
        operation_description="Update brand",
        request_body=BrandSerializer,
        responses={
            200: BrandSerializer,
            400: "Bad request",
        }
    )
    def put(self, request: Request, pk: int):
        brand = Brand.objects.get(id=pk)
        serializer = BrandSerializer(instance=brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)
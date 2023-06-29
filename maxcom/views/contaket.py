from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Contaket,
)
from ..serializers import (
    ContaketSerializer,
)

class ContaketCreateView(APIView):
    @swagger_auto_schema(
        request_body=ContaketSerializer,
        operation_description="Create new contaket",
        operation_summary="Create new contaket",
        responses={
            201: ContaketSerializer,
            400: "Bad request"
        }
    )
    def post(self, request:Request):
        data = request.data
        serializer = ContaketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)
    
class ContaketUpdateView(APIView):
    @swagger_auto_schema(
        request_body=ContaketSerializer,
        operation_description="Update contaket",
        operation_summary="Update contaket",
        responses={
            200: ContaketSerializer,
            400: "Bad request"
        }
    )
    def put(self, request:Request, pk:int):
        contaket = Contaket.objects.get(pk=pk)
        contaket.email = request.data['email']
        contaket.phone = request.data['phone']
        contaket.address = request.data['address']
        contaket.map = request.data['map']
        contaket.facebook = request.data['facebook']
        contaket.instagram = request.data['instagram']
        contaket.telegram = request.data['telegram']
        contaket.save()
        serializer = ContaketSerializer(contaket)
        return Response(serializer.data, status=status.HTTP_200_OK,)
    
class ContaketGetView(APIView):
    @swagger_auto_schema(
        operation_description="Get contaket",
        operation_summary="Get contaket",
        responses={
            200: ContaketSerializer,
            400: "Bad request"
        }
    )
    def get(self, request:Request):
        contaket = Contaket.objects.all()
        serializer = ContaketSerializer(contaket, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK,)
    
class ContaketGetIdView(APIView):
    @swagger_auto_schema(
        operation_description="Get contaket by id",
        operation_summary="Get contaket by id",
        responses={
            200: ContaketSerializer,
            400: "Bad request"
        }
    )
    def get(self, request:Request, pk:int):
        contaket = Contaket.objects.get(pk=pk)
        serializer = ContaketSerializer(contaket)
        return Response(serializer.data, status=status.HTTP_200_OK,)
    
class ContaketDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete contaket",
        operation_summary="Delete contaket",
        responses={
            204: "No content",
            400: "Bad request"
        }
    )
    def delete(self, request:Request, pk:int):
        contaket = Contaket.objects.get(pk=pk)
        contaket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,)


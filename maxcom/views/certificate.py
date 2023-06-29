from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Certificate,
)
from ..serializers import (
    CertificateSerializer,
)

class CertificateCreateView(APIView):
    @swagger_auto_schema(
        request_body=CertificateSerializer,
        operation_description="Create new certificate",
        operation_summary="Create new certificate",
        responses={
            201: CertificateSerializer,
            400: "Bad request"
        }
    )
    def post(self, request:Request):
        data = request.data
        serializer = CertificateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)
    
class CertificateUpdateView(APIView):
    @swagger_auto_schema(
        request_body=CertificateSerializer,
        operation_description="Update certificate",
        operation_summary="Update certificate",
        responses={
            200: CertificateSerializer,
            400: "Bad request"
        }
    )
    def put(self, request:Request, pk:int):
        certificate = Certificate.objects.get(pk=pk)
        certificate.name = request.data['name']
        certificate.image = request.data['image']
        certificate.save()
        serializer = CertificateSerializer(certificate)
        return Response(serializer.data, status=status.HTTP_200_OK,)
    
class CertificateGetView(APIView):
    @swagger_auto_schema(
        operation_description="Get certificate",
        operation_summary="Get certificate",
        responses={
            200: CertificateSerializer,
            400: "Bad request"
        }
    )
    def get(self, request:Request):
        certificate = Certificate.objects.all()
        serializer = CertificateSerializer(certificate, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK,)
    
class CertificateGetIdView(APIView):
    @swagger_auto_schema(
        operation_description="Get certificate by id",
        operation_summary="Get certificate by id",
        responses={
            200: CertificateSerializer,
            400: "Bad request"
        }
    )
    def get(self, request:Request, pk:int):
        certificate = Certificate.objects.get(pk=pk)
        serializer = CertificateSerializer(certificate)
        return Response(serializer.data, status=status.HTTP_200_OK,)
    
class CertificateDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete certificate",
        operation_summary="Delete certificate",
        responses={
            204: "No content",
            400: "Bad request"
        }
    )
    def delete(self, request:Request, pk:int):
        certificate = Certificate.objects.get(pk=pk)
        certificate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,)
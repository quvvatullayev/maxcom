from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    CompanyQuestion,
)
from ..serializers import (
    CompanyQuestionSerializer,
)

class CompanyQuestionCreateView(APIView):
    @swagger_auto_schema(
        request_body=CompanyQuestionSerializer,
        operation_description="Create new companyquestion",
        operation_summary="Create new companyquestion",
        responses={
            201: CompanyQuestionSerializer,
            400: "Bad request"
        }
    )
    def post(self, request:Request):
        data = request.data
        serializer = CompanyQuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)
    
class CompanyQuestionUpdateView(APIView):
    @swagger_auto_schema(
        request_body=CompanyQuestionSerializer,
        operation_description="Update companyquestion",
        operation_summary="Update companyquestion",
        responses={
            200: CompanyQuestionSerializer,
            400: "Bad request"
        }
    )
    def put(self, request:Request, pk:int):
        companyquestion = CompanyQuestion.objects.get(pk=pk)
        companyquestion.question = request.data['question']
        companyquestion.answer = request.data['answer']
        companyquestion.save()
        serializer = CompanyQuestionSerializer(companyquestion)
        return Response(serializer.data, status=status.HTTP_200_OK,)

class CompanyQuestionGetView(APIView):
    @swagger_auto_schema(
        operation_description="Get companyquestion",
        operation_summary="Get companyquestion",
        responses={
            200: CompanyQuestionSerializer,
            400: "Bad request"
        }
    )
    def get(self, request:Request):
        companyquestion = CompanyQuestion.objects.all()
        serializer = CompanyQuestionSerializer(companyquestion, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK,)

class CompanyQuestionGetIdView(APIView):
    @swagger_auto_schema(
        operation_description="Get companyquestion by id",
        operation_summary="Get companyquestion by id",
        responses={
            200: CompanyQuestionSerializer,
            400: "Bad request"
        }
    )
    def get(self, request:Request, pk:int):
        companyquestion = CompanyQuestion.objects.get(pk=pk)
        serializer = CompanyQuestionSerializer(companyquestion)
        return Response(serializer.data, status=status.HTTP_200_OK,)
    
class CompanyQuestionDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete companyquestion",
        operation_summary="Delete companyquestion",
        responses={
            204: "No content",
            400: "Bad request"
        }
    )
    def delete(self, request:Request, pk:int):
        companyquestion = CompanyQuestion.objects.get(pk=pk)
        companyquestion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,)
        
    
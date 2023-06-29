from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from ..serializers import (
    UserSerializer,
)

class UserCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Create new user",
        request_body=UserSerializer,
        responses={
            201: UserSerializer,
            400: "Bad request",
        }
    )
    def post(self, request: Request) -> Response:
        if User.objects.filter(username=request.data['username']):
            return Response({"message": "You are already logged in"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = Token.objects.create(user=serializer.instance)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Login user",
        request_body=UserSerializer,
        responses={
            200: UserSerializer,
            400: "Bad request",
        }
    )
    def post(self, request:Request):
        user = request.user
        token = Token.objects.create(user=user)
        return Response({'token':token.key}, status=status.HTTP_200_OK)
    
class UserLogOutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Logout user",
        responses={
            200: "Logout",
            400: "Bad request",
        }
    )
    def post(self, request:Request):
        user = request.user
        token = Token.objects.get(user = user)
        token.delete()
        return Response({'message':'Logout'}, status=status.HTTP_200_OK)
    
class UserListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Get all users",
        responses={
            200: UserSerializer,
            400: "Bad request",
        }
    )
    def get(self, request:Request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserAddAdminView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Add admin",
        responses={
            200: UserSerializer,
            400: "Bad request",
        }
    )
    def post(self, request:Request, pk:int):
        r_user:User = request.user
        if r_user.is_staff and r_user.is_superuser:
            user = User.objects.get(id=pk)
            user.is_staff = True
            user.save()
            return Response({'message':'You are admin'}, status=status.HTTP_200_OK)
        return Response({'message':'You are not admin'}, status=status.HTTP_400_BAD_REQUEST)
        
class UserDeleteAdminView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Delete admin",
        responses={
            200: UserSerializer,
            400: "Bad request",
        }
    )
    def post(self, request:Request, pk:int):
        r_user:User = request.user
        if r_user.is_staff and r_user.is_superuser:
            user = User.objects.get(id=pk)
            user.is_staff = False
            user.save()
            return Response({'message':'You are not admin'}, status=status.HTTP_200_OK)
        return Response({'message':'You are admin'}, status=status.HTTP_400_BAD_REQUEST)








        
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from ..models import (
    Card,
    Product,
)
from ..serializers import (
    CardSerializer,
    CreateCardSerializer,
)

class CardCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    @swagger_auto_schema(
        request_body=CreateCardSerializer,
        operation_description="Create new card",
        operation_summary="Create new card",
        responses={
            201: CardSerializer,
            400: "Bad request"
        }
    )
    def post(self, request: Request):
        user = request.user
        data = request.data
        data['user'] = user.id

        chack = Card.objects.filter(product=data['product'], user=data['user'])
        if chack:
            chack[0].cout += 1
            chack[0].save()
            serializer = CardSerializer(chack[0])
            return Response(serializer.data, status=status.HTTP_201_CREATED,)
        else:        
            serializer = CreateCardSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED,)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)
        
class CardUpdateView(APIView):
    authentication_classes = [TokenAuthentication]
    @swagger_auto_schema(
        request_body=CreateCardSerializer,
        operation_description="Update card",
        operation_summary="Update card",
        responses={
            200: CardSerializer,
            400: "Bad request"
        }
    )
    def put(self, request: Request, pk: int):
        user = request.user
        data = request.data
        data['user'] = user.id
        try:
            card = Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,)
        if card.user.id == user.id:
            serializer = CreateCardSerializer(card, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK,)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)
        return Response(status=status.HTTP_400_BAD_REQUEST,)
    
class CardDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    @swagger_auto_schema(
        operation_description="Delete card",
        operation_summary="Delete card",
        responses={
            204: "No content",
            400: "Bad request"
        }
    )
    def delete(self, request: Request, pk: int):
        user = request.user
        try:
            card = Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,)
        if card.user.id == user.id:
            card.delete()
            return Response(status=status.HTTP_204_NO_CONTENT,)
        return Response(status=status.HTTP_400_BAD_REQUEST,)
    
class CardGetIdView(APIView):
    authentication_classes = [TokenAuthentication]
    @swagger_auto_schema(
        operation_description="Get card by id",
        operation_summary="Get card by id",
        responses={
            200: CardSerializer,
            400: "Bad request"
        }
    )
    def get(self, request: Request, pk: int):
        user = request.user
        try:
            card = Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,)
        if card.user.id == user.id:
            serializer = CardSerializer(card)
            return Response(serializer.data, status=status.HTTP_200_OK,)
        return Response(status=status.HTTP_400_BAD_REQUEST,)
    
class CardGetView(APIView):
    authentication_classes = [TokenAuthentication]
    @swagger_auto_schema(
        operation_description="Get all cards",
        operation_summary="Get all cards",
        responses={
            200: CardSerializer,
            400: "Bad request"
        }
    )
    def get(self, request: Request):
        user = request.user
        cards = Card.objects.filter(user=user)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK,)
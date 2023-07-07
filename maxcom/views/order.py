from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
import smtplib
from ..models import (
    Card,
    Product,
    Order,
)

from ..serializers import (
    CardSerializer,
    CreateCardSerializer,
    OrderSerializer,
    CreateOrderSerializer,
    ProductSerializer,
    CreateProductSerializer,
)

class OrderCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    @swagger_auto_schema(
        request_body=CreateOrderSerializer,
        operation_description="Create new order",
        operation_summary="Create new order",
        responses={
            201: OrderSerializer,
            400: "Bad request"
        }
    )
    def post(self, request: Request):
        user = request.user
        data = request.data
        data['user'] = user.id

        card = Card.objects.filter(user=data['user'], product = data['product'])
        total = 0
        for i in card:
            total += i.product.price * i.cout
        data['total'] = total
        serializer = CreateOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            card.delete()

            sender = "quvvatullayev@gmail.com"
            receiver = user.email

            message = f"""\
            Subject: Hi Mailtrap
            To: {receiver}
            From: {sender}

            user = {user.name}\n
            product = {data['product']["name"]}\n
            brand = {data['product']['brand']}\n
            description = {data['product']['description']}\n
            price = {data['product']['price']}
            address = {data['address']}\n
            phone = {data['phone']}\n
            date = {data['date']}\n
            total = {data['total']}\n
            count = {data['cout']*data['product']['price']}"""

            with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
                auth = server.login("e83e926941c981", "268821db4f6c1f")
                send = server.sendmail(sender, receiver, message)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST,)
    
class OrderDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    @swagger_auto_schema(
        operation_description="Delete order",
        operation_summary="Delete order",
        responses={
            200: "OK",
            400: "Bad request"
        }
    )
    def delete(self, request: Request, pk: int):
        user = request.user
        order = Order.objects.filter(user=user.id, id=pk)
        if order:
            order.delete()
            return Response(status=status.HTTP_200_OK,)
        return Response(status=status.HTTP_400_BAD_REQUEST,)
    
class OrderGetView(APIView):
    authentication_classes = [TokenAuthentication]
    @swagger_auto_schema(
        operation_description="Get order",
        operation_summary="Get order",
        responses={
            200: OrderSerializer,
            400: "Bad request"
        }
    )
    def get(self, request: Request):
        user = request.user
        order = Order.objects.filter(user=user.id)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK,)
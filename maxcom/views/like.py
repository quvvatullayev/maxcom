from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from ..models import (
    Like,
    Product,
)
from ..serializers import (
    LikeSerializer,
    CreateLikeSerializer,
)

class LikeCreateView(APIView):
    @swagger_auto_schema(
        request_body=CreateLikeSerializer,
        operation_description="Create new like",
        operation_summary="Create new like",
        responses={
            201: LikeSerializer,
            400: "Bad request"
        }
    )
    def post(self, request: Request):
        data = request.data
        product = data['like_product']
        if Product.objects.get(pk=product).likes == False:
            Product.objects.filter(pk=product).update(likes=True)
            serializer = CreateLikeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            Product.objects.filter(pk=product).update(likes=False)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class LikeDeleteView(APIView):
    @swagger_auto_schema(
        operation_description="Delete like",
        operation_summary="Delete like",
        responses={
            200: "OK",
            400: "Bad request"
        }
    )
    def delete(self, request: Request, pk: int):
        like = Like.objects.get(pk=pk)
        like.delete()
        return Response(status=status.HTTP_200_OK)

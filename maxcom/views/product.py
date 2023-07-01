from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..models import (
    Product,
    ProductImage,
    Category,
    SubCategory,
    Certificate,
    Contaket,
)
from ..serializers import (
    ProductSerializer,
    CreateProductSerializer,
    ProductImageSerializer,
    CategorySerializer,
    SubCategorySerializer,
    CertificateSerializer,
    ContaketSerializer,
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

        short_description = product.short_description.split(';')
        short_description_data = []
        for short in short_description:
            short_data = {}
            short_data[short.split('==')[0].strip()] = short.split('==')[1].strip()
            short_description_data.append(short_data)

        product.short_description = short_description_data

        breand = product.brand
        breand = Product.objects.filter(brand=breand)
        serializer_breand = ProductSerializer(breand, many=True)

        subcategory_id = product.subcategory.id
        subproducts = Product.objects.filter(subcategory=subcategory_id)
        serializer_subproducts = ProductSerializer(subproducts, many=True)

        # You may like it
        category_id = product.subcategory.category.id
        subcategorys = SubCategory.objects.filter(category=category_id)
        serializer_subcategorys = SubCategorySerializer(subcategorys, many=True)
        product_subcategorys = []
        for subcategory in serializer_subcategorys.data:
            subcategory_id = subcategory['id']
            subproducts = Product.objects.filter(subcategory=subcategory_id)
            if subproducts:
                serializer_subproducts = ProductSerializer(subproducts, many=True)
                product_subcategorys.append(serializer_subproducts.data[:1])


        data = {
            'product': serializer.data,
            'product_image': serializer_image.data,
            'breand': serializer_breand.data,
            'recommend': serializer_subproducts.data[-10:],
            'product_subcategorys': product_subcategorys[:10],
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
    
class ProductGetSubCategoryView(APIView):
    @swagger_auto_schema(
        operation_description="Get products by subcategory",
        operation_summary="Get products by subcategory",
        responses={
            200:openapi.Response(
            description="Get products by subcategory",
            examples={
                "application/json": {
                    "products": [
                        {
                            "id": 1,
                            "subcategory": 1,
                            "name": "product name",
                            "brand": "product brand",
                            "description": "product description",
                            "price": 1000.0,
                            "discount": 0.0,
                            "image": "http://",
                            "short_description": "product short description",
                            "live": False,
                            "likes": False,
                            "status": False
                        }
                    ],
                    "categorys": [
                        {
                            "id": 1,
                            "name": "category name",
                            "description": "category description",
                            "image": "http://",
                            "sub_category": [
                                {
                                    "id": 1,
                                    "category": 1,
                                    "name": "subcategory name",
                                    "description": "subcategory description"
                                }
                            ]
                        }
                    ],
                    "certificate": [
                        {
                            "id": 1,
                            "name": "certificate name",
                            "image": "http://"
                        }
                    ],
                    "contact": [
                        {
                            "id": 1,
                            "name": "contact name",
                            "phone": "contact phone",
                            "email": "contact email",
                            "address": "contact address",
                            "facebook": "contact facebook",
                            "instagram": "contact instagram",
                            "telegram": "contact telegram",
                            "map": "contact map"
                        }
                    ]
                }
            }
        )
    }
    )
    def get(self, request: Request, pk: int):
        products = Product.objects.filter(subcategory=pk)
        serializer = ProductSerializer(products, many=True)

        # categorys
        categorys = Category.objects.all()
        serializer_categorys = CategorySerializer(categorys, many=True)

        categorys_list = []
        for category in serializer_categorys.data:
            category_id = category['id']
            
            sub_category = SubCategory.objects.filter(category=category_id)
            serializer_SubCategorys = SubCategorySerializer(sub_category, many=True)

            category['sub_category'] = serializer_SubCategorys.data
            categorys_list.append(category)

        # Certificate
        certificate = Certificate.objects.all()
        certificate_serializer = CertificateSerializer(certificate, many = True)

        # contact
        contact = Contaket.objects.all()
        serializer_contact = ContaketSerializer(contact, many=True)

        data = {
            'products': serializer.data,
            'categorys': categorys_list,
            'certificate': certificate_serializer.data,
            'contact': serializer_contact.data,
        }
        
        
        return Response(data, status=status.HTTP_200_OK)
    
class ProductGetBrandView(APIView):
    @swagger_auto_schema(
        operation_description="Get products by brand",
        operation_summary="Get products by brand",
        responses={
            200: ProductSerializer,
            400: "Bad request"
        }
    )
    def get(self, request: Request, pk: int):
        products = Product.objects.filter(brand_img=pk)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



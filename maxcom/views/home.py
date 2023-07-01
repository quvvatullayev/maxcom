from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.db.models import Q
# this is home page
from ..models import (
    Product,
    Category,
    SubCategory,
    ProductImage,
    Like,
    Card,
    Order,
    Certificate,
    Contaket,
    About,
    CompanyQuestion,
    Brand,
)
from ..serializers import (
    ProductSerializer,
    ProductImageSerializer,
    LikeSerializer,
    CardSerializer,
    OrderSerializer,
    CertificateSerializer,
    ContaketSerializer,
    AboutSerializer,
    CompanyQuestionSerializer,
    CategorySerializer,
    SubCategorySerializer,
    BrandSerializer,
)

class HomeView(APIView): 
    @swagger_auto_schema(
        operation_description="Home page",
        operation_summary="Home page",
        responses={
            200: openapi.Response(
                description="Get all product",
                examples={
                    "application/json": {
                        "products_deduct": [
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
                        "products_new": [
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
                        ],
                        "categorys": [
                            {
                                "id": 1,
                                "name": "category name",
                                "image": "http://",
                                "sub_category": [
                                    {
                                        "id": 1,
                                        "name": "sub category name",
                                        "category": 1
                                    }
                                ]
                            }
                        ],
                        "most_sold_product": [
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
                        "certificate": [
                            {
                                "id": 1,
                                "name": "certificate name",
                                "image": "http://"
                            }
                        ],
                        'brands':[
                            {
                                "id": 1,
                                "name": "brand name",
                                "image": "http://"
                            }
                        ]
                    }
                }
            ),

            400: "Bad request"
        }
    )
    def get(self, request:Request):
        # deduct
        # fjilter discount > 0
        products_deduct = Product.objects.filter(discount__gt=0, status=False)
        serializer_deduct = ProductSerializer(products_deduct, many=True)

        #  new products 
        products_new = Product.objects.filter(status=False)
        serializer_new = ProductSerializer(products_new, many=True)

        # contact
        contact = Contaket.objects.all()
        serializer_contact = ContaketSerializer(contact, many=True)

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

        # Most sold
        order_all = Order.objects.all()
        orders = OrderSerializer(order_all, many = True)

        product_order_id = []
        for order in orders.data:
            if order['product']['id'] not in product_order_id:
                product_order_id.append(order['product']['id'])
        product_order_id = sorted(product_order_id, reverse=True)

        most_sold_product = []
        for product in product_order_id[:5]:
            product = Product.objects.get(id = product)
            product_serializer = ProductSerializer(product)
            most_sold_product.append(product_serializer.data)

        # Certificate
        certificate = Certificate.objects.all()
        certificate_serializer = CertificateSerializer(certificate, many = True)
        
        # Brand
        brands = Brand.objects.all()
        brand_serializer = BrandSerializer(brands, many = True)
            
        data = {
            'products_deduct': serializer_deduct.data,
            'products_new': serializer_new.data[:8],
            'contact': serializer_contact.data,
            'categorys': categorys_list,
            'most_sold_product':most_sold_product,
            'certificate':certificate_serializer.data,
            'brands':brand_serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)

class SearchView(APIView):
    @swagger_auto_schema(
        operation_description="Search product",
        operation_summary="Search product",
        responses={
            200: ProductSerializer(many=True),
            400: "Bad request"
        }
    )
    def get(self, request:Request):
        query = request.GET.get('query')
        print(query)
        products = Product.objects.filter(
            Q(name__icontains              = query) |
            Q(description__icontains       = query) |
            Q(brand__icontains             = query) ,   
            )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

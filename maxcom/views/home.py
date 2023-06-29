from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
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
)

class HomeView(APIView):
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
        
            
        data = {
            'products_deduct': serializer_deduct.data,
            'products_new': serializer_new.data[:8],
            'contact': serializer_contact.data,
            'categorys': categorys_list,
            'most_sold_product':most_sold_product,
            'certificate':certificate_serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)


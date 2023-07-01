from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Category,
    SubCategory,
    Product,
    ProductImage,
    Like,
    Card,
    Certificate,
    Contaket,
    About,
    CompanyQuestion,
    Order,
    CallBack,
    Brand,
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = SubCategory
        fields = ['id', 'category', 'name', 'description']
    
class CreateSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'subcategory', 'name', 'brand', 'description', 'price', 'discount', 'image', 'short_description', 'live', 'likes', 'status']

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductImageSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']

class CreateProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = serializers.StringRelatedField()
    class Meta:
        model = Like
        fields = ['id', 'product', 'user']

class CreateLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

class CardSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = serializers.StringRelatedField()
    class Meta:
        model = Card
        fields = ['id', 'product', 'cout', 'user']

class CreateCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = ['id', 'product', 'user', ]

class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"

class ContaketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contaket
        fields = "__all__"

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"

class CompanyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyQuestion
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']       

class CallBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallBack
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
    
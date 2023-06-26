from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField(default=0)
    image = models.ImageField(upload_to='products',)
    short_description = models.CharField(max_length=1000)
    live = models.BooleanField(default=False)
    likes = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')

    def __str__(self) -> str:
        return self.product.name
    
class Like(models.Model):
    like_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.like_product.name

class Card(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cout = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cout = models.IntegerField(default=1)
    total = models.FloatField()
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product.name
    
class Certificate(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to = 'certificate')

    def __str__(self) -> str:
        return self.name
    
class Contaket(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    map = models.CharField(max_length=1000)
    facebook = models.CharField(max_length=1000)
    instagram = models.CharField(max_length=1000)
    telegram = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.email
    
class About(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    
class CompanyQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self) -> str:
        return self.question

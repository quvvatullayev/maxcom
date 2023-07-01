from django.contrib import admin

# Register your models here.
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

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Like)
admin.site.register(Card)
admin.site.register(Order)
admin.site.register(Certificate)
admin.site.register(Contaket)
admin.site.register(About)
admin.site.register(CompanyQuestion)
admin.site.register(CallBack)
admin.site.register(Brand)

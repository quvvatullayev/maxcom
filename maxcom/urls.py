from django.urls import path
from .views.category import(
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    CategoryGetIdView,
    CategoryGetView,
)

urlpatterns = [
    path('category/create/', CategoryCreateView.as_view()),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view()),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view()),
    path('category/get/<int:pk>/', CategoryGetIdView.as_view()),
    path('category/get/', CategoryGetView.as_view()),
]

from .views.subcategory import(
    SubCategoryCreateView,
    SubCategoryUpdateView,
    SubCategoryDeleteView,
    SubCategoryGetIdView,
    SubCategoryGetView,
)

urlpatterns += [
    path('subcategory/create/', SubCategoryCreateView.as_view()),
    path('subcategory/update/<int:pk>/', SubCategoryUpdateView.as_view()),
    path('subcategory/delete/<int:pk>/', SubCategoryDeleteView.as_view()),
    path('subcategory/get/<int:pk>/', SubCategoryGetIdView.as_view()),
    path('subcategory/get/', SubCategoryGetView.as_view()),
]

from .views.product import(
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductGetIdView,
    ProductGetView,
)

urlpatterns += [
    path('product/create/', ProductCreateView.as_view()),
    path('product/update/<int:pk>/', ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view()),
    path('product/get/<int:pk>/', ProductGetIdView.as_view()),
    path('product/get/', ProductGetView.as_view()),
]

from .views.productimg import(
    ProductImageCreateView,
    ProductImageUpdateView,
    ProductImageDeleteView,
    ProductImageGetIdView,
    ProductImageGetView,
)

urlpatterns += [
    path('productimage/create/', ProductImageCreateView.as_view()),
    path('productimage/update/<int:pk>/', ProductImageUpdateView.as_view()),
    path('productimage/delete/<int:pk>/', ProductImageDeleteView.as_view()),
    path('productimage/get/<int:pk>/', ProductImageGetIdView.as_view()),
    path('productimage/get/', ProductImageGetView.as_view()),
]

from .views.like import(
    LikeCreateView,
    LikeDeleteView,
)

urlpatterns += [
    path('like/create/', LikeCreateView.as_view()),
    path('like/delete/<int:pk>/', LikeDeleteView.as_view()),
]
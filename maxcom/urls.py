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
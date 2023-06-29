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
    ProductGetSubCategoryView,
)

urlpatterns += [
    path('product/create/', ProductCreateView.as_view()),
    path('product/update/<int:pk>/', ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view()),
    path('product/get/<int:pk>/', ProductGetIdView.as_view()),
    path('product/get/', ProductGetView.as_view()),
    path('product/get/subcategory/<int:pk>/', ProductGetSubCategoryView.as_view()),
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

from .views.card import(
    CardCreateView,
    CardUpdateView,
    CardDeleteView,
    CardGetIdView,
    CardGetView,
)

urlpatterns += [
    path('card/create/', CardCreateView.as_view()),
    path('card/update/<int:pk>/', CardUpdateView.as_view()),
    path('card/delete/<int:pk>/', CardDeleteView.as_view()),
    path('card/get/<int:pk>/', CardGetIdView.as_view()),
    path('card/get/', CardGetView.as_view()),
]

from .views.order import(
    OrderCreateView,
    OrderDeleteView,
    OrderGetView,
)

urlpatterns += [
    path('order/create/', OrderCreateView.as_view()),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view()),
    path('order/get/', OrderGetView.as_view()),
]

from .views.certificate import(
    CertificateCreateView,
    CertificateUpdateView,
    CertificateGetView,
    CertificateGetIdView,
    CertificateDeleteView,
)

urlpatterns += [
    path('certificate/create/', CertificateCreateView.as_view()),
    path('certificate/update/<int:pk>/', CertificateUpdateView.as_view()),
    path('certificate/get/', CertificateGetView.as_view()),
    path('certificate/get/<int:pk>/', CertificateGetIdView.as_view()),
    path('certificate/delete/<int:pk>/', CertificateDeleteView.as_view()),
]

from .views.contaket import(
    ContaketCreateView,
    ContaketUpdateView,
    ContaketGetView,
    ContaketGetIdView,
    ContaketDeleteView,
)

urlpatterns += [
    path('contaket/create/', ContaketCreateView.as_view()),
    path('contaket/update/<int:pk>/', ContaketUpdateView.as_view()),
    path('contaket/get/', ContaketGetView.as_view()),
    path('contaket/get/<int:pk>/', ContaketGetIdView.as_view()),
    path('contaket/delete/<int:pk>/', ContaketDeleteView.as_view()),
]

from .views.about import(
    AboutCreateView,
    AboutUpdateView,
    AboutGetView,
    AboutGetIdView,
    AboutDeleteView,
)

urlpatterns += [
    path('about/create/', AboutCreateView.as_view()),
    path('about/update/<int:pk>/', AboutUpdateView.as_view()),
    path('about/get/', AboutGetView.as_view()),
    path('about/get/<int:pk>/', AboutGetIdView.as_view()),
    path('about/delete/<int:pk>/', AboutDeleteView.as_view()),
]

from .views.companyquestion import(
    CompanyQuestionCreateView,
    CompanyQuestionUpdateView,
    CompanyQuestionGetView,
    CompanyQuestionGetIdView,
    CompanyQuestionDeleteView,
)

urlpatterns += [
    path('companyquestion/create/', CompanyQuestionCreateView.as_view()),
    path('companyquestion/update/<int:pk>/', CompanyQuestionUpdateView.as_view()),
    path('companyquestion/get/', CompanyQuestionGetView.as_view()),
    path('companyquestion/get/<int:pk>/', CompanyQuestionGetIdView.as_view()),
    path('companyquestion/delete/<int:pk>/', CompanyQuestionDeleteView.as_view()),
]

from .views.home import(
    HomeView,
)

urlpatterns += [
    path('', HomeView.as_view()),
]

from .views.userauth import(
    UserCreateView,
    UserLoginView,
    UserLogOutView,
)

urlpatterns += [
    path('user/create/', UserCreateView.as_view()),
    path('user/login/', UserLoginView.as_view()),
    path('user/logout/', UserLogOutView.as_view()),
]

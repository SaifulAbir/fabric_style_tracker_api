from django.urls import path
from supplier.api import SupplierListAPI, SupplierCreateAPI, SupplierUpdateAPI, CountryListAPI, SupplierTypeListAPI, \
    SupplierTypeCreateAPI, SupplierTypeUpdateAPI

urlpatterns = [
    path('supplier/list/', SupplierListAPI.as_view()),
    path('supplier_type/create/', SupplierTypeCreateAPI.as_view()),
    path('supplier_type/update/<str:pk>/', SupplierTypeUpdateAPI.as_view()),
    path('supplier_type/list/', SupplierTypeListAPI.as_view()),
    path('country/list/', CountryListAPI.as_view()),
    path('supplier/create/', SupplierCreateAPI.as_view()),
    path('supplier/update/<str:pk>/', SupplierUpdateAPI.as_view()),
]
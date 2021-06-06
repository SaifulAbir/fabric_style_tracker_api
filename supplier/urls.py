from django.urls import path
from supplier.api import SupplierListAPI, SupplierCreateAPI, SupplierUpdateAPI, CountryListAPI, SupplierTypeListAPI

urlpatterns = [
    path('supplier/list/', SupplierListAPI.as_view()),
    path('supplier_type/list/', SupplierTypeListAPI.as_view()),
    path('country/list/', CountryListAPI.as_view()),
    path('supplier/create/', SupplierCreateAPI.as_view()),
    path('supplier/update/<str:pk>/', SupplierUpdateAPI.as_view()),
]
from django.urls import path
from fabric.api import FabricCreateAPI, FabricListAPI, SupplierListAPI, FabricCompositionListAPI, FabricTypeListAPI, \
    FabricUpdateAPI

urlpatterns = [
    path('fabric/create/', FabricCreateAPI.as_view()),
    path('fabric/update/<str:pk>/', FabricUpdateAPI.as_view()),
    path('fabric/list/', FabricListAPI.as_view()),
    path('supplier/list/', SupplierListAPI.as_view()),
    path('fabric_composition/list/', FabricCompositionListAPI.as_view()),
    path('fabric_type/list/', FabricTypeListAPI.as_view()),
]
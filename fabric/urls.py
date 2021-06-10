from django.urls import path
from fabric.api import FabricCreateAPI, FabricListAPI, FabricCompositionListAPI, FabricTypeListAPI, \
    FabricUpdateAPI, FabricTypeCreateAPI, FabricTypeUpdateAPI, FabricCompositionCreateAPI, FiberPercentageListAPI, \
    FiberPercentageCreateAPI, FiberPercentageUpdateAPI, FiberListAPI, FabricCompositionUpdateAPI

urlpatterns = [
    path('fabric/create/', FabricCreateAPI.as_view()),
    path('fabric/update/<str:pk>/', FabricUpdateAPI.as_view()),
    path('fabric_type/create/', FabricTypeCreateAPI.as_view()),
    path('fabric_type/update/<str:pk>/', FabricTypeUpdateAPI.as_view()),
    path('fabric_composition/create/', FabricCompositionCreateAPI.as_view()),
    path('fabric_composition/update/<str:pk>/', FabricCompositionUpdateAPI.as_view()),
    path('fabric/list/', FabricListAPI.as_view()),
    path('fabric_composition/list/', FabricCompositionListAPI.as_view()),
    path('fabric_type/list/', FabricTypeListAPI.as_view()),
    path('fiber/list/', FiberListAPI.as_view()),
    path('fiber_percentage/list/', FiberPercentageListAPI.as_view()),
    path('fiber_percentage/create/', FiberPercentageCreateAPI.as_view()),
    path('fiber_percentage/update/<str:pk>/', FiberPercentageUpdateAPI.as_view()),
]
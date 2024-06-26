from django.urls import path
from fabric.api import FabricCreateAPI, FabricListAPI, FabricCompositionListAPI, FabricTypeListAPI, \
    FabricUpdateAPI, FabricTypeCreateAPI, FabricTypeUpdateAPI, FabricCompositionCreateAPI, FiberPercentageListAPI, \
    FiberPercentageCreateAPI, FiberPercentageUpdateAPI, FiberListAPI, FabricCompositionUpdateAPI, FiberCreateAPI, \
    FiberUpdateAPI, FabricCreateFromExcelAPI, DownloadFabricExcelFormat, DashboardAPI, FabricDetailAPI, \
    AppearanceListAPI, WeaveListAPI, WeaveUpdateAPI, AppearanceUpdateAPI, AppearanceCreateAPI, WeaveCreateAPI, \
    FabricMillAndDekkoReferenceListAPI, FabricSearchAPI

urlpatterns = [
    path('fabric/create/', FabricCreateAPI.as_view()),
    path('fabric/create_from_excel/', FabricCreateFromExcelAPI),
    path('fabric/fabric_excel_format/', DownloadFabricExcelFormat.as_view()),
    path('fabric/search/', FabricSearchAPI.as_view()),
    path('fabric/update/<str:pk>/', FabricUpdateAPI.as_view()),
    path('fabric_type/create/', FabricTypeCreateAPI.as_view()),
    path('fabric_type/update/<str:pk>/', FabricTypeUpdateAPI.as_view()),
    path('fabric_composition/create/', FabricCompositionCreateAPI.as_view()),
    path('fabric_composition/update/<str:pk>/', FabricCompositionUpdateAPI.as_view()),
    path('fabric/list/', FabricListAPI.as_view()),
    path('fabric_mill_and_dekko_reference/list/', FabricMillAndDekkoReferenceListAPI.as_view()),
    path('fabric/get/<str:pk>/', FabricDetailAPI.as_view()),
    path('fabric_composition/list/', FabricCompositionListAPI.as_view()),
    path('fabric_type/list/', FabricTypeListAPI.as_view()),
    path('fiber/create/', FiberCreateAPI.as_view()),
    path('fiber/list/', FiberListAPI.as_view()),
    path('fiber/update/<str:pk>/', FiberUpdateAPI.as_view()),
    path('fiber_percentage/list/', FiberPercentageListAPI.as_view()),
    path('fiber_percentage/create/', FiberPercentageCreateAPI.as_view()),
    path('fiber_percentage/update/<str:pk>/', FiberPercentageUpdateAPI.as_view()),
    path('dashboard/', DashboardAPI.as_view()),
    path('weave/create/', WeaveCreateAPI.as_view()),
    path('weave/update/<str:pk>/', WeaveUpdateAPI.as_view()),
    path('weave/list/', WeaveListAPI.as_view()),
    path('appearance/create/', AppearanceCreateAPI.as_view()),
    path('appearance/update/<str:pk>/', AppearanceUpdateAPI.as_view()),
    path('appearance/list/', AppearanceListAPI.as_view()),
]
from django.urls import path
from style.api import StyleListAPI, StyleCreateAPI, StyleUpdateAPI, WashTypeListAPI, DesignerListAPI, PropertyListAPI, \
    WashTypeCreateAPI, WashTypeUpdateAPI, DesignerCreateAPI, DesignerUpdateAPI, PropertyCreateAPI, PropertyUpdateAPI, \
    StyleNameListAPI, StyleSearchAPI

urlpatterns = [
    path('style/list/', StyleListAPI.as_view()),
    path('style/name/list/', StyleNameListAPI.as_view()),
    path('style/create/', StyleCreateAPI.as_view()),
    path('style/update/<str:pk>/', StyleUpdateAPI.as_view()),
    path('style/search/', StyleSearchAPI.as_view()),
    path('wash_type/create/', WashTypeCreateAPI.as_view()),
    path('wash_type/update/<str:pk>/', WashTypeUpdateAPI.as_view()),
    path('wash_type/list/', WashTypeListAPI.as_view()),
    path('designer/create/', DesignerCreateAPI.as_view()),
    path('designer/update/<str:pk>/', DesignerUpdateAPI.as_view()),
    path('designer/list/', DesignerListAPI.as_view()),
    path('property/create/', PropertyCreateAPI.as_view()),
    path('property/update/<str:pk>/', PropertyUpdateAPI.as_view()),
    path('property/list/', PropertyListAPI.as_view()),
]
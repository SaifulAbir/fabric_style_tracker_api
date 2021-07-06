from django.urls import path
from style.api import StyleListAPI, StyleCreateAPI, StyleUpdateAPI, WashTypeListAPI, DesignerListAPI, PropertyListAPI

urlpatterns = [
    path('style/list/', StyleListAPI.as_view()),
    path('style/create/', StyleCreateAPI.as_view()),
    path('style/update/<str:pk>/', StyleUpdateAPI.as_view()),
    path('wash_type/list/', WashTypeListAPI.as_view()),
    path('designer/list/', DesignerListAPI.as_view()),
    path('property/list/', PropertyListAPI.as_view()),
]
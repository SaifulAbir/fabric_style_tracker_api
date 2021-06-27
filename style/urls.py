from django.urls import path
from style.api import StyleListAPI, StyleCreateAPI, StyleUpdateAPI
urlpatterns = [
    path('style/list/', StyleListAPI.as_view()),
    path('style/create/', StyleCreateAPI.as_view()),
    path('style/update/<str:pk>/', StyleUpdateAPI.as_view()),
]
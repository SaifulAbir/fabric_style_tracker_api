from django.urls import path
from fabric.api import FabricCreateAPI

urlpatterns = [
    path('fabric/create/', FabricCreateAPI.as_view())
]
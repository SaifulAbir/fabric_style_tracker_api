from rest_framework_simplejwt.views import TokenObtainPairView
from account.serializers import CustomTokenObtainPairSerializer, ChangePasswordSerializer
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


# def is_superuser(user):
#     return user.groups.filter(name='general').exists()
#
#
# from rest_framework_simplejwt.authentication import JWTAuthentication
#
# class P7Authentication(JWTAuthentication):
#     def authenticate(self, request):
#         return super(P7Authentication, self).authenticate(request)
#
#
# class ProfessionalAuthentication(P7Authentication):
#     def authenticate(self, request):
#         result = super(ProfessionalAuthentication, self).authenticate(request)
#         if result is not None:
#             user = result[0]
#             if is_superuser(user):
#                 return result
#         return None


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    # permission_classes = (IsAuthenticated,)
    # permission_classes = (ProfessionalAuthentication)
    serializer_class = ChangePasswordSerializer
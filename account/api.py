from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password, check_password
from account.serializers import CustomTokenObtainPairSerializer, ChangePasswordSerializer, UserSerializer
from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer


class UserListAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegistration(CreateAPIView):
    def post(self, request, *args, **kwargs):
        data_status = {}
        user_data = request.data
        try:
            user = User.objects.get(username=user_data['username'])
            user_exist = True
            user_active = user.is_active
        except User.DoesNotExist:
            user_exist = False
            user_active = False

        if user_exist and user_active:
            data_status["message"] = "Username already exist"
            return Response(data_status)

        hash_password = make_password(user_data['password'])
        if not user_exist:
            user = User(first_name=user_data['first_name'], last_name=user_data['last_name'], username=user_data['username'], password=hash_password,
                        is_active=0)
            user.save()

        data = {
            'status': 'success',
            'code': HTTP_200_OK,
            "message": 'Registration successful. Please contact to admin for account approval.',
            "result": {
                "user": {
                    "username": user_data['username'],
                    "user_id": user.id,
                }
            }
        }
        return Response(data)
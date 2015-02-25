from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserSerializer


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)
        account = authenticate(username=username, password=password)
        if account is not None:
            if account.is_active:
                login(request, account)
                serialized_account = UserSerializer(account)
                return Response(serialized_account.data,
                                status=status.HTTP_200_OK)
            else:
                return Response({
                                'status': 'Unauthorized',
                                'message': 'This account is disabled'
                                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                            'status': 'Unauthorized',
                            'message': 'Username/password combination is wrong'
                            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):

    def get(self, request, format=None):
        logout(request)
        return Response({'message': 'User Logged Out'},
                        status=status.HTTP_204_NO_CONTENT)

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.models import CustomUser
from users.serializers import UserSerializers


class UserViewSets(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        if request.data.get('email') is None:
            raise AuthenticationFailed(detail="Campo email é obrigatório", code=status.HTTP_401_UNAUTHORIZED)

        if request.data.get('password') is None:
            raise AuthenticationFailed(detail="Campo password é obrigatório", code=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(username=request.data['email'], password=request.data['password'])

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Credenciais inválidas'}, status=401)

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated  # <-- Here
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from api_user_auth.serializers import SignInSerializers, SignUpSerializers


class Logout(APIView):
    # Check headers Authorization: user's token (Authenticated User)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        # delete user's token in DB
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class LoginView(APIView):
    serializer_class = SignInSerializers

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

    def post(self, request, format=None):
        # get token by register User
        token = None
        user_data = SignInSerializers(data=request.data)
        if user_data.is_valid(raise_exception=True):
            user = authenticate(request, username=user_data.validated_data['username'],
                                password=user_data.validated_data['password'])
            token = Token.objects.get_or_create(user=user)[0].key

        if not token:
            return Response({'msg':'no token'})
        return Response({
            'token': token,
        })


class RegisterView(APIView):
    """
        Registers a new user.
        """
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializers

    def post(self, request):
        """
        Creates a new User object.
        Username, email, and password are required.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )

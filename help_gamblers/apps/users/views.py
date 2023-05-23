import logging

from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from help_gamblers.apps.core.serializers import CurrencySerializer, LanguageSerializer
from help_gamblers.apps.users.models import User
from help_gamblers.apps.users.serializers import SignUpSerializer, ConfirmAccountSerializer, ForgotPasswordSerializer, \
    ResetPasswordSerializer, UserSerializer

log = logging.getLogger(__name__)


class LoginAPIView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': {
                'id': user.pk,
                'email': user.email,
                'name': user.name,
                'currency': CurrencySerializer(user.currency).data if user.currency else None,
                'language': LanguageSerializer(user.language).data if user.language else None,
            }
        })


class SignUpAPIView(APIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request):
        """
        ---
        request_serializer: SignUpSerializer
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save_user(serializer.data)
            return JsonResponse(
                {
                    'result': 'success',
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmAccountAPIView(APIView):
    serializer_class = ConfirmAccountSerializer
    permission_classes = [AllowAny]

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request):
        """
        ---
        request_serializer: ConfirmAccountSerializer
        """

        serializer = self.serializer_class(data=request.data, context={"request": self.request})
        if serializer.is_valid():
            user = serializer.confirm(serializer.data)
            return JsonResponse(
                user,
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordAPIView(APIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = [AllowAny]

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request):
        """
        ---
        request_serializer: ForgotPasswordSerializer
        """

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.send_mail(serializer.data)
            return JsonResponse(
                {
                    'result': 'success',
                },
                status=status.HTTP_200_OK,
            )
        error = serializer.errors
        if serializer.errors and hasattr(serializer.errors, 'non_field_errors'):
            error = {
                "email": serializer.errors['non_field_errors'][0]
            }

        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(APIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request, reset_key_token):
        """
        ---
        request_serializer: ResetPasswordSerializer
        """
        context = {
            'request': request,
            'reset_key_token': reset_key_token,
        }
        serializer = self.serializer_class(data=request.data, context=context)
        if serializer.is_valid():
            user = User.objects.get(reset_key_token=context['reset_key_token'])
            serializer.reset(serializer.data)
            return JsonResponse(
                {
                    'email': user.email,
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]

    @action(detail=False, methods=['get'])
    def me(self, request):
        user = self.request.user
        if user:
            return Response(UserSerializer(user, context={"request": self.request}).data, status=status.HTTP_200_OK)
        return Response({"message": "User not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

import logging

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

from help_gamblers.apps.core.models import Currency, Language
from help_gamblers.apps.core.serializers import CurrencySerializer, LanguageSerializer
from help_gamblers.apps.core.utils import generate_unique_key, is_invalid_password
from help_gamblers.apps.users.models import User
from help_gamblers.apps.users.tasks import forgot_password_email

log = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, allow_null=False, allow_blank=False, )
    currency = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.all(), required=False)
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), required=False)

    def get_fields(self):
        fields = super(UserSerializer, self).get_fields()
        if self.context['request'].method == 'GET':
            fields['currency'] = CurrencySerializer()
            fields['language'] = LanguageSerializer()
        return fields

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'name',
            'language',
            'currency',
        )

    def validate(self, attrs):
        email = attrs.get('email')
        if email:
            user = User.objects.filter(email=email).first()
            if user is None:
                return attrs

            if self.context['request'].user.email == user.email:
                return attrs
            else:
                raise ValidationError('User with given email already exists.')
        return attrs


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_null=False, allow_blank=False)
    password = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    repeat_password = serializers.CharField(required=True)
    name = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
    )

    @staticmethod
    def save_user(validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.is_active = True
        user.email_confirmation_token = generate_unique_key(user.email)
        user.save()
        # send_signup_email.delay({
        #     'email': user.email,
        #     'token': user.email_confirmation_token,
        #     'name': user.name,
        # })

    @staticmethod
    def check_valid_password(data):
        invalid_password_message = is_invalid_password(data.get('password'), data.get('repeat_password'))
        if invalid_password_message:
            return invalid_password_message

    def validate(self, data):
        valid_pass = self.check_valid_password(data)
        if valid_pass:
            raise serializers.ValidationError({'password': valid_pass})
        self.check_valid_email(data['email'])

        return data

    @staticmethod
    def check_valid_email(value):
        user = User.objects.filter(email=value).first()
        if user:
            raise serializers.ValidationError({'email': ['This email address has already exist.']})


class ConfirmAccountSerializer(serializers.Serializer):
    token = serializers.CharField()

    def confirm(self, validated_data):
        user = User.objects.get(email_confirmation_token=validated_data['token'])
        user.is_active = True
        user.email_confirmation_token = None
        user.save()
        data = UserSerializer(user, context={"request": self.context.get("request")}).data
        token, created = Token.objects.get_or_create(user=user)
        data["token"] = token.key
        return data

    def validate(self, data):
        if not User.objects.filter(email_confirmation_token=data['token']).exists():
            raise serializers.ValidationError('Invalid token.')

        return data


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    @staticmethod
    def send_mail(validated_data):
        user = User.objects.get(email=validated_data['email'])
        user.reset_key_token = generate_unique_key(user.email)

        forgot_password_email.delay({
            'email': user.email,
            'token': user.reset_key_token,
            'name': user.name,
        })
        user.save()

    def validate(self, data):
        self.check_email(data['email'])

        return data

    @staticmethod
    def check_email(value):
        user = User.objects.filter(email=value)

        if not user.exists():
            raise serializers.ValidationError('This email address does not exist.')

        if not user.filter(is_active=True).exists():
            raise serializers.ValidationError('Your account is inactive.')

        return value


class ResetPasswordSerializer(serializers.Serializer):
    def confirm(self, validated_data):
        user = User.objects.get(reset_key_token=self.context['key_token'])
        user.is_active = True
        user.save()


class ReleaseAnnouncementSingleUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)


class SingleUserIdSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True, allow_null=False)

    def validate(self, attrs):
        exists = User.objects.filter(id=attrs["id"]).first()
        if not exists:
            raise ValidationError({"detail": f"User with id: {attrs['id']} not exists"})
        return attrs


class ListUserIdSerializer(serializers.Serializer):
    users_list = serializers.ListSerializer(child=SingleUserIdSerializer())


class ReleaseAnnouncementSerializer(serializers.Serializer):
    users_list = serializers.ListSerializer(child=ReleaseAnnouncementSingleUserSerializer())
    text_to_send = serializers.CharField(allow_null=False, allow_blank=False)

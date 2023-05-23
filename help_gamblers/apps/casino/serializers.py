import logging

from rest_framework import serializers

from help_gamblers.apps.casino.models import Types, AffiliateProgram, Software, Deposit, WithdrawalMethod, Casino, \
    CasinoSoftware, CasinoDeposit, CasinoWithdrawalMethod, CasinoWithdrawalTime, CasinoWithdrawalLimit, \
    CasinoAffiliateProgram, CasinoRestrictedCountry, CasinoTypes, CasinoCurrency, CasinoLanguage, CasinoLicence, \
    CasinoWhatWeLike, CasinoWhatWeDisLike
from help_gamblers.apps.core.models import Country, Currency, Language, Licence
from help_gamblers.apps.core.serializers import LanguageSerializer, LicenceSerializer, CountrySerializer, \
    CurrencySerializer

log = logging.getLogger(__name__)


class TypesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False, )

    class Meta:
        model = Types
        fields = (
            'id',
            'name',
        )


class AffiliateProgramSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False, )

    class Meta:
        model = AffiliateProgram
        fields = (
            'id',
            'name',
        )


class SoftwareSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False, )

    class Meta:
        model = Software
        fields = (
            'id',
            'name',
        )


class DepositSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False, )

    class Meta:
        model = Deposit
        fields = (
            'id',
            'name',
        )


class WithdrawalMethodSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False, )

    class Meta:
        model = WithdrawalMethod
        fields = (
            'id',
            'name',
        )


class CasinoSoftwareSerializer(serializers.ModelSerializer):
    casino = serializers.PrimaryKeyRelatedField(queryset=Casino.objects.all(), allow_null=False, )
    software = serializers.PrimaryKeyRelatedField(queryset=Software.objects.all(), allow_null=False, )

    class Meta:
        model = CasinoSoftware
        fields = (
            'id',
            'casino',
            'software',
        )


class CasinoDepositSerializer(serializers.ModelSerializer):
    casino = serializers.PrimaryKeyRelatedField(queryset=Casino.objects.all(), allow_null=False, )
    deposit = serializers.PrimaryKeyRelatedField(queryset=Deposit.objects.all(), allow_null=False, )

    class Meta:
        model = CasinoDeposit
        fields = (
            'id',
            'casino',
            'deposit',
        )


class CasinoWithdrawalMethodSerializer(serializers.ModelSerializer):
    casino = serializers.PrimaryKeyRelatedField(queryset=Casino.objects.all(), allow_null=False, )
    withdrawal_method = serializers.PrimaryKeyRelatedField(queryset=WithdrawalMethod.objects.all(), allow_null=False, )

    class Meta:
        model = CasinoWithdrawalMethod
        fields = (
            'id',
            'casino',
            'withdrawal_method',
        )


class CasinoAffiliateProgramSerializer(serializers.ModelSerializer):
    casino = serializers.PrimaryKeyRelatedField(queryset=Casino.objects.all(), allow_null=False, )
    affiliate_program = serializers.PrimaryKeyRelatedField(queryset=AffiliateProgram.objects.all(), allow_null=False, )

    class Meta:
        model = CasinoAffiliateProgram
        fields = (
            'id',
            'casino',
            'affiliate_program',
        )


class CasinoRestrictedCountrySerializer(serializers.ModelSerializer):
    casino = serializers.PrimaryKeyRelatedField(queryset=Casino.objects.all(), allow_null=False, )
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), allow_null=False, )

    class Meta:
        model = CasinoRestrictedCountry
        fields = (
            'id',
            'casino',
            'country',
        )


class CasinoTypesSerializer(serializers.ModelSerializer):
    casino = serializers.PrimaryKeyRelatedField(queryset=Casino.objects.all(), allow_null=False, )
    casino_type = serializers.PrimaryKeyRelatedField(queryset=Types.objects.all(), allow_null=False, )

    class Meta:
        model = CasinoTypes
        fields = (
            'id',
            'casino',
            'casino_type',
        )


class CasinoCurrencySerializer(serializers.ModelSerializer):
    casino = serializers.PrimaryKeyRelatedField(queryset=Casino.objects.all(), allow_null=False, )
    currency = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.all(), allow_null=False, )

    class Meta:
        model = CasinoCurrency
        fields = (
            'id',
            'casino',
            'currency',
        )


class CasinoLanguageSerializer(serializers.ModelSerializer):
    casino = serializers.PrimaryKeyRelatedField(queryset=Casino.objects.all(), allow_null=False, )
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), allow_null=False, )

    class Meta:
        model = CasinoLanguage
        fields = (
            'id',
            'casino',
            'language',
        )


class CasinoLicenceSerializer(serializers.ModelSerializer):
    casino = serializers.PrimaryKeyRelatedField(queryset=Casino.objects.all(), allow_null=False, )
    licence = serializers.PrimaryKeyRelatedField(queryset=Licence.objects.all(), allow_null=False, )

    class Meta:
        model = CasinoLicence
        fields = (
            'id',
            'casino',
            'licence',
        )


class CasinoWithdrawalTimeSerializer(serializers.ModelSerializer):
    casino = serializers.PrimaryKeyRelatedField(queryset=Casino.objects.all(), allow_null=False, )
    name = serializers.CharField(max_length=255, required=True, allow_blank=False, allow_null=False, )

    class Meta:
        model = CasinoWithdrawalTime
        fields = (
            'id',
            'casino',
            'name',
        )


class CasinoWithdrawalLimitSerializer(serializers.ModelSerializer):
    casino = serializers.PrimaryKeyRelatedField(queryset=Casino.objects.all(), allow_null=False, )
    name = serializers.CharField(max_length=255, required=True, allow_blank=False, allow_null=False, )

    class Meta:
        model = CasinoWithdrawalLimit
        fields = (
            'id',
            'casino',
            'name',
        )


class CasinoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False, )
    website = serializers.URLField(required=True, allow_null=False, allow_blank=False, )
    manual_flushing = serializers.BooleanField(required=False, allow_null=False, default=False, )
    live_chat = serializers.BooleanField(required=False, allow_null=False, default=False, )
    rtp = serializers.ChoiceField(choices=Casino.RTP_CHOICES, allow_null=False, allow_blank=False, )
    company = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False, )
    established = serializers.DateField(required=True, allow_null=False, )
    contact_email = serializers.EmailField(required=True, allow_blank=False, allow_null=False, )

    class Meta:
        model = Casino
        fields = (
            'id',
            'name',
            'website',
            'manual_flushing',
            'live_chat',
            'rtp',
            'company',
            'established',
            'contact_email',
            'image',
            'affiliate_link',
            'is_recommended',
            'rating',
            'description',
            'virtual_games_description',
            'live_gaming_description',
            'mobile_gaming_description',
            'support_description',
            'security_description',
            'payment_info_description',
        )


class CasinoLanguageGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)
    language = LanguageSerializer(read_only=True)

    class Meta:
        model = CasinoLanguage
        fields = (
            'id',
            'casino',
            'language',
        )


class CasinoLicenceGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)
    licence = LicenceSerializer(read_only=True)

    class Meta:
        model = CasinoLicence
        fields = (
            'id',
            'casino',
            'licence',
        )


class CasinoAffiliateProgramGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)
    affiliate_program = AffiliateProgramSerializer(read_only=True)

    class Meta:
        model = CasinoAffiliateProgram
        fields = (
            'id',
            'casino',
            'affiliate_program',
        )


class CasinoRestrictedCountryGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = CasinoRestrictedCountry
        fields = (
            'id',
            'casino',
            'country',
        )


class CasinoTypesGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)
    casino_type = TypesSerializer(read_only=True)

    class Meta:
        model = CasinoTypes
        fields = (
            'id',
            'casino',
            'casino_type',
        )


class CasinoDepositGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)
    deposit = DepositSerializer(read_only=True)

    class Meta:
        model = CasinoDeposit
        fields = (
            'id',
            'casino',
            'deposit',
        )


class CasinoCurrencyGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)
    currency = CurrencySerializer(read_only=True)

    class Meta:
        model = CasinoCurrency
        fields = (
            'id',
            'casino',
            'currency',
        )


class CasinoWithdrawalMethodGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)
    withdrawal_method = WithdrawalMethodSerializer(read_only=True)

    class Meta:
        model = CasinoWithdrawalMethod
        fields = (
            'id',
            'casino',
            'withdrawal_method',
        )


class CasinoWithdrawalTimeGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)

    class Meta:
        model = CasinoWithdrawalTime
        fields = (
            'id',
            'casino',
            'name',
        )


class CasinoWithdrawalLimitGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)

    class Meta:
        model = CasinoWithdrawalLimit
        fields = (
            'id',
            'casino',
            'name',
        )


class CasinoSoftwareGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)
    software = SoftwareSerializer(read_only=True)

    class Meta:
        model = CasinoSoftware
        fields = (
            'id',
            'casino',
            'software',
        )


class CasinoWhatWeLikeGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)

    class Meta:
        model = CasinoWhatWeLike
        fields = (
            'id',
            'casino',
            'name',
        )


class CasinoWhatWeDisLikeGetSerializer(serializers.ModelSerializer):
    casino = CasinoSerializer(read_only=True)

    class Meta:
        model = CasinoWhatWeDisLike
        fields = (
            'id',
            'casino',
            'name',
        )

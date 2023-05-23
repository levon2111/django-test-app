import logging

from rest_framework import serializers

from help_gamblers.apps.core.models import Country, Currency, Language, Licence

log = logging.getLogger(__name__)


class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False, )

    class Meta:
        model = Country
        fields = (
            'id',
            'name',
            'iso',
            'iso3',
            'iso_numeric',
            'fips',
            'capital',
            'area',
            'population',
            'continent',
            'tld',
            'currency_code',
            'currency_symbol',
            'currency_name',
            'phone',
            'postal_code_format',
            'postal_code_regex',
            'languages',
            'geonameid',
            'neighbours',
            'equivalent_fips_code',
        )


class CurrencySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False, )

    class Meta:
        model = Currency
        fields = (
            'id',
            'name',
            'code',
            'symbol',
            'factor',
            'is_active',
            'is_base',
            'is_default',
            'info',
        )


class LanguageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False, )

    class Meta:
        model = Language
        fields = (
            'id',
            'name',
            'iso_639_1',
            'iso_639_2T',
            'iso_639_2B',
            'iso_639_3',
            'name_en',
            'name_native',
            'family',
            'notes',
            'countries_spoken',
        )


class LicenceSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True, allow_null=False, allow_blank=False, )

    class Meta:
        model = Licence
        fields = (
            'id',
            'name',
        )

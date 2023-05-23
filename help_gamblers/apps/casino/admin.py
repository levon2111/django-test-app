from django.contrib import admin
from django.contrib.admin import ModelAdmin

from help_gamblers.apps.casino.models import Types, AffiliateProgram, Software, Deposit, WithdrawalMethod, Casino, \
    CasinoSoftware, CasinoDeposit, CasinoWithdrawalMethod, CasinoWithdrawalTime, CasinoWithdrawalLimit, \
    CasinoAffiliateProgram, CasinoRestrictedCountry, CasinoTypes, CasinoCurrency, CasinoLanguage, CasinoLicence, \
    CasinoWhatWeLike, CasinoWhatWeDisLike


@admin.register(Types)
class TypesAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
        "created",
        "modified",
    ]


@admin.register(AffiliateProgram)
class AffiliateProgramAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
        "created",
        "modified",
    ]


@admin.register(Software)
class SoftwareAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
        "created",
        "modified",
    ]


@admin.register(Deposit)
class DepositAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
        "created",
        "modified",
    ]


@admin.register(WithdrawalMethod)
class WithdrawalMethodAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
        "created",
        "modified",
    ]


@admin.register(Casino)
class CasinoAdmin(ModelAdmin):
    list_display = [
        "id",
        "country",
        "name",
        "website",
        "manual_flushing",
        "rtp",
        "company",
        "established",
        "live_chat",
        "contact_email",
        "description",
        "restricted_countries_description",
        "virtual_games_description",
        "live_gaming_description",
        "mobile_gaming_description",
        "support_description",
        "security_description",
        "payment_info_description",
        "created",
        "modified",
    ]


@admin.register(CasinoSoftware)
class CasinoSoftwareAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "software",
        "created",
        "modified",
    ]


@admin.register(CasinoDeposit)
class CasinoDepositAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "deposit",
        "created",
        "modified",
    ]


@admin.register(CasinoWithdrawalMethod)
class CasinoWithdrawalMethodAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "withdrawal_method",
        "created",
        "modified",
    ]


@admin.register(CasinoWithdrawalTime)
class CasinoWithdrawalTimeAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "name",
        "created",
        "modified",
    ]


@admin.register(CasinoWithdrawalLimit)
class CasinoWithdrawalLimitAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "name",
        "created",
        "modified",
    ]


@admin.register(CasinoAffiliateProgram)
class CasinoAffiliateProgramAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "affiliate_program",
        "created",
        "modified",
    ]


@admin.register(CasinoRestrictedCountry)
class CasinoRestrictedCountryAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "country",
        "created",
        "modified",
    ]


@admin.register(CasinoTypes)
class CasinoTypesAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "casino_type",
        "created",
        "modified",
    ]


@admin.register(CasinoCurrency)
class CasinoCurrencyAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "currency",
        "created",
        "modified",
    ]


@admin.register(CasinoLanguage)
class CasinoLanguageAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "language",
        "created",
        "modified",
    ]


@admin.register(CasinoLicence)
class CasinoLicenceAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "licence",
        "created",
        "modified",
    ]


@admin.register(CasinoWhatWeLike)
class CasinoWhatWeLikeAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "name",
    ]


@admin.register(CasinoWhatWeDisLike)
class CasinoWhatWeDisLikeAdmin(ModelAdmin):
    list_display = [
        "id",
        "casino",
        "name",
    ]

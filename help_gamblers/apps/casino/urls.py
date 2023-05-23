from rest_framework import routers

from help_gamblers.apps.casino.views import TypesModelViewSet, AffiliateProgramModelViewSet, SoftwareModelViewSet, \
    DepositModelViewSet, WithdrawalMethodModelViewSet, CasinoModelViewSet, CasinoSoftwareModelViewSet, \
    CasinoDepositModelViewSet, CasinoWithdrawalMethodModelViewSet, CasinoWithdrawalTimeModelViewSet, \
    CasinoWithdrawalLimitModelViewSet, CasinoAffiliateProgramModelViewSet, CasinoRestrictedCountryModelViewSet, \
    CasinoTypesModelViewSet, CasinoCurrencyModelViewSet, CasinoLanguageModelViewSet

router = routers.DefaultRouter()
router.register("types", TypesModelViewSet)
router.register("affiliate-program", AffiliateProgramModelViewSet)
router.register("software", SoftwareModelViewSet)
router.register("deposit", DepositModelViewSet)
router.register("withdrawal-method", WithdrawalMethodModelViewSet)
router.register("casino", CasinoModelViewSet)
router.register("casino-software", CasinoSoftwareModelViewSet)
router.register("casino-deposit", CasinoDepositModelViewSet)
router.register("casino-withdrawal-method", CasinoWithdrawalMethodModelViewSet)
router.register("casino-withdrawal-time", CasinoWithdrawalTimeModelViewSet)
router.register("casino-withdrawal-limit", CasinoWithdrawalLimitModelViewSet)
router.register("casino-affiliate-program", CasinoAffiliateProgramModelViewSet)
router.register("casino-restricted-country", CasinoRestrictedCountryModelViewSet)
router.register("casino-types", CasinoTypesModelViewSet)
router.register("casino-currency", CasinoCurrencyModelViewSet)
router.register("casino-language", CasinoLanguageModelViewSet)

app_name = 'casino'

urlpatterns = [
]

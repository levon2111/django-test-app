from rest_framework import routers

from help_gamblers.apps.core.views import CountryModelViewSet, CurrencyModelViewSet, LanguageModelViewSet, \
    LicenceModelViewSet

router = routers.DefaultRouter()
router.register("country", CountryModelViewSet)
router.register("currency", CurrencyModelViewSet)
router.register("language", LanguageModelViewSet)
router.register("licence", LicenceModelViewSet)

app_name = 'core'

urlpatterns = [
]

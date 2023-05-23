from rest_framework import status
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from help_gamblers.apps.casino.filters import CasinoFilter
from help_gamblers.apps.casino.models import Types, AffiliateProgram, Software, Deposit, WithdrawalMethod, Casino, \
    CasinoSoftware, CasinoDeposit, CasinoWithdrawalMethod, CasinoWithdrawalTime, CasinoWithdrawalLimit, \
    CasinoAffiliateProgram, CasinoRestrictedCountry, CasinoTypes, CasinoCurrency, CasinoLanguage, CasinoLicence
from help_gamblers.apps.casino.serializers import TypesSerializer, AffiliateProgramSerializer, SoftwareSerializer, \
    DepositSerializer, WithdrawalMethodSerializer, CasinoSerializer, CasinoSoftwareSerializer, CasinoDepositSerializer, \
    CasinoWithdrawalMethodSerializer, CasinoWithdrawalTimeSerializer, CasinoWithdrawalLimitSerializer, \
    CasinoAffiliateProgramSerializer, CasinoRestrictedCountrySerializer, CasinoTypesSerializer, \
    CasinoCurrencySerializer, CasinoLanguageSerializer, CasinoLicenceSerializer, CasinoLanguageGetSerializer, \
    CasinoLicenceGetSerializer, CasinoAffiliateProgramGetSerializer, CasinoRestrictedCountryGetSerializer, \
    CasinoTypesGetSerializer, CasinoDepositGetSerializer, CasinoCurrencyGetSerializer, \
    CasinoWithdrawalMethodGetSerializer, CasinoWithdrawalTimeGetSerializer, CasinoWithdrawalLimitGetSerializer, \
    CasinoSoftwareGetSerializer, CasinoWhatWeLikeGetSerializer, CasinoWhatWeDisLikeGetSerializer
from help_gamblers.apps.core.paginator import LimitOffsetPaginationNew


class TypesModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = Types.objects.all()
    serializer_class = TypesSerializer
    permission_classes = [AllowAny, ]


class AffiliateProgramModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = AffiliateProgram.objects.all()
    serializer_class = AffiliateProgramSerializer
    permission_classes = [AllowAny, ]


class SoftwareModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    permission_classes = [AllowAny, ]


class DepositModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [AllowAny, ]


class WithdrawalMethodModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = WithdrawalMethod.objects.all()
    serializer_class = WithdrawalMethodSerializer
    permission_classes = [AllowAny, ]


class CasinoModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = Casino.objects.all()
    serializer_class = CasinoSerializer
    permission_classes = [AllowAny, ]
    filterset_class = CasinoFilter
    pagination_class = LimitOffsetPaginationNew

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def _paginate_queryset(self, queryset):
        return self.paginator.paginate_queryset(queryset, self.request, limit=queryset.count(), offset=0, view=self)

    def paginate_queryset(self, queryset):
        if 'all' in self.request.query_params:
            return self._paginate_queryset(queryset)
        self.pagination_class = LimitOffsetPagination
        return super().paginate_queryset(queryset)

    @action(detail=True)
    def general_information(self, request, pk=None):
        data = {}
        casino = Casino.objects.filter(pk=pk).first()
        if casino:
            data["website"] = casino.website
            languages = casino.casino_languages.all()
            pluses = casino.pluses.all()
            minuses = casino.minuses.all()
            data["pluses"] = CasinoWhatWeLikeGetSerializer(pluses, many=True).data
            data["minuses"] = CasinoWhatWeDisLikeGetSerializer(minuses, many=True).data
            data["languages"] = CasinoLanguageGetSerializer(languages, many=True).data
            data["established"] = casino.established

            data["description"] = casino.description
            data["virtual_games_description"] = casino.virtual_games_description
            data["live_gaming_description"] = casino.live_gaming_description
            data["mobile_gaming_description"] = casino.mobile_gaming_description
            data["support_description"] = casino.support_description
            data["security_description"] = casino.security_description
            data["payment_info_description"] = casino.payment_info_description

            data["company"] = casino.company
            casino_licences = casino.casino_licences.all()
            data["licences"] = CasinoLicenceGetSerializer(casino_licences, many=True).data
            affiliate_programs = casino.affiliate_programs
            restricted_countries = casino.restricted_countries
            casino_types = casino.casino_types
            data["affiliate_programs"] = CasinoAffiliateProgramGetSerializer(affiliate_programs, many=True).data
            data["restricted_countries"] = CasinoRestrictedCountryGetSerializer(restricted_countries, many=True).data
            data["casino_types"] = CasinoTypesGetSerializer(casino_types, many=True).data

        else:
            return Response({"detail": f"Casino with id {pk} not found."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True)
    def payment_information(self, request, pk=None):
        data = {}
        casino = Casino.objects.filter(pk=pk).first()
        if casino:
            deposit_methods = casino.deposits.all()
            casino_currencies = casino.casino_currencies.all()
            withdrawal_methods = casino.withdrawal_methods.all()
            withdrawal_times = casino.withdrawal_times.all()
            withdrawal_limits = casino.withdrawal_limits.all()
            data["deposit_methods"] = CasinoDepositGetSerializer(deposit_methods, many=True).data
            data["casino_currencies"] = CasinoCurrencyGetSerializer(casino_currencies, many=True).data
            data["withdrawal_methods"] = CasinoWithdrawalMethodGetSerializer(withdrawal_methods, many=True).data
            data["withdrawal_times"] = CasinoWithdrawalTimeGetSerializer(withdrawal_times, many=True).data
            data["withdrawal_limits"] = CasinoWithdrawalLimitGetSerializer(withdrawal_limits, many=True).data
        else:
            return Response({"detail": f"Casino with id {pk} not found."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True)
    def games_information(self, request, pk=None):
        data = {}
        casino = Casino.objects.filter(pk=pk).first()
        if casino:
            softwares = casino.softwares.all()
            data["softwares"] = CasinoSoftwareGetSerializer(softwares, many=True).data
            data["rtp"] = casino.rtp
        else:
            return Response({"detail": f"Casino with id {pk} not found."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True)
    def customer_support_information(self, request, pk=None):
        data = {}
        casino = Casino.objects.filter(pk=pk).first()
        if casino:
            data["live_chat"] = casino.live_chat
            data["contact_email"] = casino.contact_email
        else:
            return Response({"detail": f"Casino with id {pk} not found."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)


class CasinoSoftwareModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = CasinoSoftware.objects.all()
    serializer_class = CasinoSoftwareSerializer
    permission_classes = [AllowAny, ]


class CasinoDepositModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = CasinoDeposit.objects.all()
    serializer_class = CasinoDepositSerializer
    permission_classes = [AllowAny, ]


class CasinoWithdrawalMethodModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = CasinoWithdrawalMethod.objects.all()
    serializer_class = CasinoWithdrawalMethodSerializer
    permission_classes = [AllowAny, ]


class CasinoWithdrawalTimeModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = CasinoWithdrawalTime.objects.all()
    serializer_class = CasinoWithdrawalTimeSerializer
    permission_classes = [AllowAny, ]


class CasinoWithdrawalLimitModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = CasinoWithdrawalLimit.objects.all()
    serializer_class = CasinoWithdrawalLimitSerializer
    permission_classes = [AllowAny, ]


class CasinoAffiliateProgramModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = CasinoAffiliateProgram.objects.all()
    serializer_class = CasinoAffiliateProgramSerializer
    permission_classes = [AllowAny, ]


class CasinoRestrictedCountryModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = CasinoRestrictedCountry.objects.all()
    serializer_class = CasinoRestrictedCountrySerializer
    permission_classes = [AllowAny, ]


class CasinoTypesModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = CasinoTypes.objects.all()
    serializer_class = CasinoTypesSerializer
    permission_classes = [AllowAny, ]


class CasinoCurrencyModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = CasinoCurrency.objects.all()
    serializer_class = CasinoCurrencySerializer
    permission_classes = [AllowAny, ]


class CasinoLanguageModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = CasinoLanguage.objects.all()
    serializer_class = CasinoLanguageSerializer
    permission_classes = [AllowAny, ]


class CasinoLicenceModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = CasinoLicence.objects.all()
    serializer_class = CasinoLicenceSerializer
    permission_classes = [AllowAny, ]

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from help_gamblers.apps.core.models import Country, Currency, Language, Licence
from help_gamblers.apps.core.paginator import LimitOffsetPaginationNew
from help_gamblers.apps.core.serializers import CountrySerializer, CurrencySerializer, LanguageSerializer, \
    LicenceSerializer


class CountryModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [AllowAny, ]
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


class CurrencyModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [AllowAny, ]
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


class LanguageModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = Language.objects.filter(iso_639_1__in=['en', 'de', 'ru'])
    serializer_class = LanguageSerializer
    permission_classes = [AllowAny, ]
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


class LicenceModelViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'put', 'post', 'delete', ]
    queryset = Licence.objects.all()
    serializer_class = LicenceSerializer
    permission_classes = [AllowAny, ]

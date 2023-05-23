from distutils.util import strtobool

import django_filters

from help_gamblers.apps.casino.models import Casino
from help_gamblers.apps.core.models import Country


class CasinoFilter(django_filters.FilterSet):
    BOOLEAN_CHOICES = (('false', 'False'), ('true', 'True'),)

    is_recommended = django_filters.TypedChoiceFilter(
        choices=BOOLEAN_CHOICES,
        coerce=strtobool,
        method='get_is_recommended',
    )
    country = django_filters.ModelChoiceFilter(queryset=Country.objects.all())

    def get_is_recommended(self, queryset, name, value):
        if value:
            return queryset.filter(is_recommended=True)
        return queryset.filter(is_recommended=False)

    class Meta:
        model = Casino
        fields = {
            'name': ['exact', 'contains'],
        }

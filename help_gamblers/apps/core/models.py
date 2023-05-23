import logging

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils.translation import gettext as _

log = logging.getLogger(__name__)


class AbstractBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(models.Model):
    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ['name']

    iso = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3, unique=True)
    iso_numeric = models.IntegerField(unique=True)
    fips = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255, unique=True)
    capital = models.CharField(max_length=255, blank=True, null=True)
    area = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    continent = models.CharField(max_length=2, blank=True, null=True)
    tld = models.CharField(max_length=255, blank=True, null=True)
    currency_code = models.CharField(max_length=3, blank=True, null=True)
    currency_symbol = models.CharField(max_length=255, blank=True, null=True)
    currency_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    postal_code_format = models.CharField(max_length=255, blank=True, null=True)
    postal_code_regex = models.CharField(max_length=255, blank=True, null=True)
    languages = models.CharField(max_length=255, blank=True, null=True)
    geonameid = models.IntegerField(blank=True, null=True)
    neighbours = models.CharField(max_length=255, blank=True, null=True)
    equivalent_fips_code = models.CharField(max_length=4, blank=True, null=True)

    @staticmethod
    def get_by_request(request) -> 'Country':
        """Get a Country object from `request`, via the COUNTRIES_PLUS_COUNTRY_HEADER"""

        country = None
        default_iso = None

        try:
            header_name = settings.COUNTRIES_PLUS_COUNTRY_HEADER
        except AttributeError:
            raise AttributeError(
                "COUNTRIES_PLUS_COUNTRY_HEADER setting missing.  This setting must be present "
                "when using the countries_plus middleware."
            )

        if not header_name:
            raise AttributeError(
                "COUNTRIES_PLUS_COUNTRY_HEADER can not be empty.   This setting must be present "
                "when using the countries_plus middleware."
            )

        try:
            default_iso = settings.COUNTRIES_PLUS_DEFAULT_ISO.upper()
        except AttributeError:
            pass

        geoip_request_iso = request.META.get(header_name, '')
        if geoip_request_iso:
            try:
                country = Country.objects.get(iso=geoip_request_iso.upper())
            except ObjectDoesNotExist:
                pass

        if not country:
            log.warning(
                f"countries_plus:  Could not find a country matching '{geoip_request_iso}' from provided meta "
                f"header '{header_name}'."
            )
            if default_iso:
                log.warning(
                    f"countries_plus:  Setting country to provided default '{default_iso}'."
                )
                try:
                    country = Country.objects.get(iso=default_iso)
                except ObjectDoesNotExist:
                    log.warning(
                        f"countries_plus:  Could not find a country matching COUNTRIES_PLUS_DEFAULT_ISO "
                        f"of '{default_iso}'."
                    )
        return country

    def __str__(self):
        return self.name


class CurrencyQuerySet(models.QuerySet):

    def active(self):
        return self.filter(is_active=True)

    def default(self):
        return self.get(is_default=True)

    def base(self):
        return self.get(is_base=True)


class CurrencyManager(models.Manager):

    def get_queryset(self):
        return CurrencyQuerySet(self.model, using=self._db).active()

    def default(self):
        return self.get_queryset().default()

    def base(self):
        return self.get_queryset().base()


class Currency(models.Model):
    code = models.CharField(_('code'), max_length=3)
    name = models.CharField(_('name'), max_length=55, db_index=True)
    symbol = models.CharField(_('symbol'), max_length=4, blank=True, db_index=True)
    factor = models.DecimalField(_('factor'), max_digits=30, decimal_places=10, default=1.0,
                                 help_text=_('Specifies the currency rate ratio to the base currency.'))

    is_active = models.BooleanField(_('active'), default=True, help_text=_('The currency will be available.'))
    is_base = models.BooleanField(_('base'), default=False,
                                  help_text=_('Make this the base currency against which rate factors are calculated.'))
    is_default = models.BooleanField(_('default'), default=False,
                                     help_text=_('Make this the default user currency.'))

    # Used to store other available information about a currency
    info = models.JSONField(blank=True, default=dict)
    objects = models.Manager()
    active = CurrencyManager()

    class Meta:
        ordering = ['name']
        verbose_name = _('currency')
        verbose_name_plural = _('currencies')

    def __str__(self):
        return self.code

    def save(self, **kwargs):
        # Make sure the base and default currencies are unique
        if self.is_base is True:
            self.__class__._default_manager.filter(is_base=True).update(is_base=False)

        if self.is_default is True:
            self.__class__._default_manager.filter(is_default=True).update(is_default=False)

        # Make sure default / base currency is active
        if self.is_default or self.is_base:
            self.is_active = True

        super(Currency, self).save(**kwargs)


class Language(models.Model):
    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")
        ordering = ["name_en"]

    country = None

    iso_639_1 = models.CharField(max_length=2)
    iso_639_2T = models.CharField(max_length=3, unique=True, blank=True)
    iso_639_2B = models.CharField(max_length=3, unique=True, blank=True)
    iso_639_3 = models.CharField(max_length=3, blank=True)
    name_en = models.CharField(max_length=100)
    name_native = models.CharField(max_length=100)
    family = models.CharField(max_length=50)
    notes = models.CharField(max_length=100, blank=True)
    countries_spoken = models.ManyToManyField(Country, blank=True)

    @property
    def iso(self) -> str:
        return self.iso_639_1

    @property
    def name(self) -> str:
        return self.name_native

    def __str__(self) -> str:
        return self.name_en


class Licence(AbstractBaseModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "licences"

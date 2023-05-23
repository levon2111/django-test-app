from django.contrib import admin
from django.contrib.admin import ModelAdmin

from help_gamblers.apps.core.models import Country, Currency, Language, Licence


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = ("id", "continent", "name", "iso", "iso3", "languages", "currency_name")
    list_display_links = ("name",)
    search_fields = ("name", "iso", "iso3")
    list_filter = ("continent",)


@admin.register(Currency)
class CurrencyAdmin(ModelAdmin):
    list_display = ("name", "is_active", "is_base", "is_default", "code", "symbol", "factor")
    list_filter = ("is_active",)
    search_fields = ("name", "code")


@admin.register(Language)
class LanguageAdmin(ModelAdmin):
    list_display = [
        "id",
        "name_en",
        "iso_639_1",
        "iso_639_2T",
        "iso_639_2B",
        "iso_639_3",
        "name_native",
        "family",
        "notes",
    ]
    list_display_links = ("name_en",)
    search_fields = ("name_en", "name_native")


@admin.register(Licence)
class LicenceAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
        "created",
        "modified",
    ]

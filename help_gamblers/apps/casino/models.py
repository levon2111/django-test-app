from django.db import models

from help_gamblers.apps.core.models import AbstractBaseModel, Country, Currency, Language, Licence


class Types(AbstractBaseModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class AffiliateProgram(AbstractBaseModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, )

    def __str__(self):
        return self.name


class Software(AbstractBaseModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, )

    def __str__(self):
        return self.name


class Deposit(AbstractBaseModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, )

    def __str__(self):
        return self.name


class WithdrawalMethod(AbstractBaseModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True, )

    def __str__(self):
        return self.name


class Casino(AbstractBaseModel):
    NOT_STATED = 'NOT_STATED'
    RTP_CHOICES = [
        (NOT_STATED, 'NOT_STATED'),
    ]

    name = models.CharField(max_length=255, null=False, blank=False, )
    website = models.URLField(null=False, blank=False, )

    manual_flushing = models.BooleanField(default=False, )
    rtp = models.CharField(
        max_length=255,
        choices=RTP_CHOICES,
        default=NOT_STATED,
    )
    company = models.CharField(max_length=255, null=False, blank=False, )
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    established = models.DateField(null=False, blank=False, auto_now_add=True)
    live_chat = models.BooleanField(default=False, )
    contact_email = models.EmailField(null=False, blank=False, )
    image = models.URLField()
    affiliate_link = models.URLField()
    is_recommended = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    restricted_countries_description = models.TextField(null=True, blank=True)
    virtual_games_description = models.TextField(null=True, blank=True)
    live_gaming_description = models.TextField(null=True, blank=True)
    mobile_gaming_description = models.TextField(null=True, blank=True)
    support_description = models.TextField(null=True, blank=True)
    security_description = models.TextField(null=True, blank=True)
    payment_info_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "casinos"


class CasinoSoftware(AbstractBaseModel):
    casino = models.ForeignKey(Casino, on_delete=models.CASCADE, null=False, blank=False, related_name="softwares", )
    software = models.ForeignKey(Software, on_delete=models.CASCADE, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino.name}- {self.software.name}"

    class Meta:
        unique_together = ("casino", "software")


class CasinoDeposit(AbstractBaseModel):
    casino = models.ForeignKey(Casino, on_delete=models.CASCADE, null=False, blank=False, related_name="deposits", )
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino.name}- {self.deposit.name}"

    class Meta:
        unique_together = ("casino", "deposit")


class CasinoWithdrawalMethod(AbstractBaseModel):
    casino = models.ForeignKey(
        Casino,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="withdrawal_methods",
    )
    withdrawal_method = models.ForeignKey(WithdrawalMethod, on_delete=models.CASCADE, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino.name}- {self.withdrawal_method.name}"

    class Meta:
        unique_together = ("casino", "withdrawal_method")


class CasinoWithdrawalTime(AbstractBaseModel):
    casino = models.ForeignKey(
        Casino,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="withdrawal_times",
    )
    name = models.CharField(max_length=255, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino}-{self.name}"

    class Meta:
        unique_together = ("casino", "name")


class CasinoWithdrawalLimit(AbstractBaseModel):
    casino = models.ForeignKey(
        Casino,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="withdrawal_limits",
    )
    name = models.CharField(max_length=255, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino}-{self.name}"

    class Meta:
        unique_together = ("casino", "name")


class CasinoAffiliateProgram(AbstractBaseModel):
    casino = models.ForeignKey(
        Casino,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="affiliate_programs",
    )
    affiliate_program = models.ForeignKey(AffiliateProgram, on_delete=models.CASCADE, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino.name}- {self.affiliate_program.name}"

    class Meta:
        unique_together = ("casino", "affiliate_program")


class CasinoRestrictedCountry(AbstractBaseModel):
    casino = models.ForeignKey(
        Casino,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="restricted_countries",
    )
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino.name}-{self.country.name}"

    class Meta:
        unique_together = ("casino", "country",)


class CasinoTypes(AbstractBaseModel):
    casino = models.ForeignKey(
        Casino,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="casino_types",
    )
    casino_type = models.ForeignKey(Types, on_delete=models.CASCADE, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino.name}-{self.casino_type.name}"

    class Meta:
        unique_together = ("casino", "casino_type",)


class CasinoCurrency(AbstractBaseModel):
    casino = models.ForeignKey(
        Casino,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="casino_currencies",
    )
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino.name}-{self.currency.name}"

    class Meta:
        unique_together = ("casino", "currency",)


class CasinoLanguage(AbstractBaseModel):
    casino = models.ForeignKey(
        Casino,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="casino_languages",
    )
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino.name}-{self.language.name}"

    class Meta:
        unique_together = ("casino", "language",)


class CasinoLicence(AbstractBaseModel):
    casino = models.ForeignKey(
        Casino,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="casino_licences",
    )
    licence = models.ForeignKey(Licence, on_delete=models.CASCADE, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino.name}-{self.licence.name}"

    class Meta:
        unique_together = ("casino", "licence",)


class CasinoWhatWeLike(AbstractBaseModel):
    casino = models.ForeignKey(
        Casino,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="pluses",
    )
    name = models.CharField(max_length=255, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino}-{self.name}"

    class Meta:
        unique_together = ("casino", "name")


class CasinoWhatWeDisLike(AbstractBaseModel):
    casino = models.ForeignKey(
        Casino,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="minuses",
    )
    name = models.CharField(max_length=255, null=False, blank=False, )

    def __str__(self):
        return f"{self.casino}-{self.name}"

    class Meta:
        unique_together = ("casino", "name")

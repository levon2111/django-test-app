import hashlib
import random
import string
from decimal import Decimal as D, InvalidOperation, ROUND_UP

from django import forms
from django.contrib.auth import password_validation

from .conf import SESSION_KEY
from .models import Currency as C


def generate_unique_key(value, length=40):
    """
    generate key from passed value
    :param value:
    :param length: key length
    :return:
    """

    salt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(26)).encode(
        'utf-8')
    value = value.encode('utf-8')
    unique_key = hashlib.sha1(salt + value).hexdigest()

    return unique_key[:length]


def is_invalid_password(password, repeat_password):
    """
    check passwords strength and equality
    :param password:
    :param repeat_password:
    :return error message or None:
    """
    error_messages = {
        'not_match': 'Password and Repeat Password fields must match.',
    }

    if not password or (not password and not repeat_password):
        return

    error_message = ''
    try:
        password_validation.validate_password(password=password, )
    except forms.ValidationError as e:
        error_message = list(e.messages)

    if error_message:
        return forms.ValidationError(error_message)

    if password != repeat_password:
        return forms.ValidationError(error_messages['not_match'])


def get_active_currencies_qs():
    return C.active.defer('info').all()


def calculate(price, to_code, **kwargs):
    """Converts a price in the default currency to another currency"""
    qs = kwargs.get('qs', get_active_currencies_qs())
    kwargs['qs'] = qs
    default_code = qs.default().code
    return convert(price, default_code, to_code, **kwargs)


def convert(amount, from_code, to_code, decimals=2, qs=None):
    """Converts from any currency to any currency"""
    if from_code == to_code:
        return amount

    if qs is None:
        qs = get_active_currencies_qs()

    from_, to = qs.get(code=from_code), qs.get(code=to_code)

    amount = D(amount) * (to.factor / from_.factor)
    return price_rounding(amount, decimals=decimals)


def get_currency_code(request):
    for attr in ('session', 'COOKIES'):
        if hasattr(request, attr):
            try:
                return getattr(request, attr)[SESSION_KEY]
            except KeyError:
                continue

    # fallback to default...
    try:
        return C.active.default().code
    except C.DoesNotExist:
        return None  # shit happens...


def price_rounding(price, decimals=2):
    """Takes a decimal price and rounds to a number of decimal places"""
    try:
        exponent = D('.' + decimals * '0')
    except InvalidOperation:
        # Currencies with no decimal places, ex. JPY, HUF
        exponent = D()
    return price.quantize(exponent, rounding=ROUND_UP)

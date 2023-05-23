from help_gamblers.apps.core.conf import SESSION_KEY
from help_gamblers.apps.core.models import Currency
from help_gamblers.apps.core.utils import get_currency_code


def add_request_country(request):
    """Add 'country' to the request context.  Requires countries_plus middleware."""
    return {'country': getattr(request, 'country', None)}


def currencies(request):
    request.session.setdefault(SESSION_KEY, get_currency_code(False))

    try:
        currency = Currency.active.get(
            code__iexact=request.session[SESSION_KEY])
    except Currency.DoesNotExist:
        currency = None

    return {
        'CURRENCIES': Currency.active.all(),  # get all active currencies
        'CURRENCY_CODE': request.session[SESSION_KEY],
        'CURRENCY': currency,  # for backward compatibility
    }

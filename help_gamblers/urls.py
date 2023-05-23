"""help_gamblers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from help_gamblers.apps.casino.urls import router as casino_urls
from help_gamblers.apps.core.urls import router as core_urls
from help_gamblers.apps.users.urls import router as user_urls

admin.site.site_header = 'Help Gamblers'
admin.site.site_title = 'Help Gamblers'
admin.site.index_title = 'Welcome to Help Gamblers Administration'

schema_view = get_schema_view(
    openapi.Info(
        title='Help Gamblers API',
        default_version='v1',
        description='Help Gamblers api endpoints',
    ),
    validators=['flex', 'ssv'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)


class DefaultRouter(routers.DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method for extending url routes from another router.
    """

    def extend(self, app_router):
        """
        Extend the routes with url routes of the passed in router.

        Args:
             app_router: SimpleRouter instance containing route definitions.
        """
        self.registry.extend(app_router.registry)


router = DefaultRouter()
router.extend(core_urls)
router.extend(casino_urls)
router.extend(user_urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('help_gamblers.apps.users.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.yaml', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

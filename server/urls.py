from django.conf import settings
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import include, path


handler404 = 'apps.core.errors.page_not_found'  # noqa: WPS440, F811
handler500 = 'apps.core.errors.server_error'  # noqa: WPS440, F811

urlpatterns = [
    path('auth/', include('apps.users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
    path('about/', include('apps.about.urls', namespace='about')),
    path('', include('apps.recipes.urls', namespace='recipes')),
]

if settings.DEBUG:
    from django.conf.urls.static import static  # noqa: WPS433

    urlpatterns += static(  # type: ignore
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from app.routes import urlpatterns

urlpatterns += [
    path(settings.ADMIN_PATH, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

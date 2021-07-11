from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Article API",
        default_version='v1',
        description="Welcome!",
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', schema_view.with_ui()),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('user.urls')),
]

urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
urlpatterns += static(
     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)



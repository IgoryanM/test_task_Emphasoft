from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from users.views import UserModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='Test_task API',
        default_version='v1',
        description='Documentation for test_task_api',
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from employee_app.views import dashboard

schema_view = get_schema_view(
    openapi.Info(title="Employee API", default_version='v1'),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/', include('employee_app.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api-auth/', include('rest_framework.urls')),
]
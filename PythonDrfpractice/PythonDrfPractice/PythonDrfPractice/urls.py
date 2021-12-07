from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('FirstApp/', include('FirstApp.urls')),
    path('SecondApp/', include("SecondApp.urls")),
    path('ThirdApp/', include('ThirdApp.urls')),

    path('admin/', admin.site.urls),
    path('openapi/', get_schema_view(
        title="Swagger",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),

]

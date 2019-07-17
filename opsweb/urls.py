"""sqlweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

# swagger pakeage
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
# from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from apps.account.router import account_router
from apps.core.router import core_router
from apps.core.views import CoreObtainJSONWebToken


schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
router = DefaultRouter()
router.registry.extend(account_router.registry)
router.registry.extend(core_router.registry)

urlpatterns = [
    path(r'', include(router.urls)),
    path('docs/', schema_view),  # swagger doc
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # swagger login
    path('admin/', admin.site.urls),
    path('api-token-auth/', CoreObtainJSONWebToken.as_view()),
]


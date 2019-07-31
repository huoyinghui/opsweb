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
import xadmin
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
# swagger pakeage
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from core.views import CoreObtainJSONWebToken
# from core.router import core_router
from core import views as core_views
from music import views as music_views


schema_view = get_schema_view(title='Web API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
router = DefaultRouter()
router.register(r'tree', core_views.PageJsonTreeSet)
router.register(r'music', music_views.MusicViewSet)

urlpatterns = [
    path(r'api/', include(router.urls)),
    # path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('docs/', schema_view),  # swagger doc
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # swagger login
    path('api-token-auth/', CoreObtainJSONWebToken.as_view()),
]



# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^api/', include('core.urls')),
#     url(r'^docs/', include('rest_framework_swagger.urls')),
# ]


if settings.DEBUG:
    from django.contrib.staticfiles import views
    urlpatterns += [
        path(r'static/', views.serve),
    ]

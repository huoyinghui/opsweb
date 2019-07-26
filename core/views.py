from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from .models import User, PageJson
from .serializers import UserSerializers, PageJsonSerializers
from .baseviews import BaseViewSet


import logging


logger = logging.getLogger('core')


class CoreObtainJSONWebToken(ObtainJSONWebToken):
    permission_classes = [IsAdminUser]


class CoreRefreshJSONWebToken(RefreshJSONWebToken):
    permission_classes = [IsAuthenticated]


class CoreVerifyJSONWebToken(VerifyJSONWebToken):
    permission_classes = [IsAuthenticated]


# 设置jwt 权限
obtain_jwt_token = ObtainJSONWebToken.as_view()
refresh_jwt_token = RefreshJSONWebToken.as_view()
verify_jwt_token = VerifyJSONWebToken.as_view()


class CustomBackend(ModelBackend):
    """
    实现邮箱/用户名登陆
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            logger.error("{}".format(e), exc_info=True)
            return None


class UserSet(BaseViewSet):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializers
    permission_classes = [IsAdminUser]
    search_fields = ['level']


class PageJsonSet(BaseViewSet):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    queryset = PageJson.objects.all().order_by('id')
    serializer_class = PageJsonSerializers
    permission_classes = [IsAdminUser]
    search_fields = ['level']


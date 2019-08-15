import logging
from calendar import timegm
from datetime import datetime

from django.contrib import auth
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken

from core import serializers
from opsweb import errors
from opsweb.exceptions import MyException
from .baseviews import BaseViewSet
from .models import User, PageJson
from .serializers import UserSerializers, PageJsonSerializers

logger = logging.getLogger('core')


class CoreObtainJSONWebToken(ObtainJSONWebToken):
    permission_classes = [AllowAny]


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
            logger.error("CustomBackend.authenticate {}".format(e), exc_info=True)
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


# class LoginView():
#     permission_classes = ()
#     authentication_classes = ()
#     serializer_class = serializers.LoginSerializer

class PageJsonSet(BaseViewSet):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    queryset = PageJson.objects.all().order_by('id')
    serializer_class = PageJsonSerializers
    permission_classes = []
    search_fields = ['level']


class PageJsonTreeSet(PageJsonSet):
    """

    """
    page_query_param = 'page'

    def serialize_tree(self, queryset):
        for obj in queryset:
            data = self.get_serializer(obj).data
            data['children'] = self.serialize_tree(obj.children.all())
            yield data

    def list(self, request):
        """
        This text is the description for this API
        ---
        param1 -- A first parameter
        param2 -- A second parameter
        """
        queryset = self.get_queryset().filter(level=0)
        data = self.serialize_tree(queryset)
        return Response(data)

    def retrieve(self, request, pk=None):
        obj = self.get_object()
        data = self.serialize_tree([obj])
        return Response(data)


class LoginView(generics.GenericAPIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        """
        用户名密码登录

        ---
        serializer: serializers.LoginSerializer

        """
        logger.debug('LoginView request data:%s', request.data)
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                # tasks.user_init.delay(user.id)
            else:
                raise MyException(_('username or password is error'), errors.Account.USERNAME_OR_PASSWORD)

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            # Include original issued at time for a brand new token,
            # to allow token refresh
            if api_settings.JWT_ALLOW_REFRESH:
                payload['orig_iat'] = timegm(
                    datetime.utcnow().utctimetuple()
                )
            token = jwt_encode_handler(payload)
            logger.debug('LoginView login ok')
            serializer = serializers.LoginSerializer(
                {'token': token, 'user': user}, context={'request': request})

            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.debug('LoginView LoginSerializer invalid')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

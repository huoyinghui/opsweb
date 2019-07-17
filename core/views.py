from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from .models import Boss, User
from .serializers import BossSerializers
from .baseviews import BaseViewSet


class ListBoss(BaseViewSet):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    queryset = Boss.objects.all().order_by('id')
    serializer_class = BossSerializers
    permission_classes = [IsAdminUser]
    search_fields = ['level']

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        print(request, format)
        bossnames = [boss.boss_name for boss in Boss.objects.all()]
        return Response(bossnames)


class CoreObtainJSONWebToken(ObtainJSONWebToken):
    permission_classes = [IsAuthenticated]


class CoreRefreshJSONWebToken(RefreshJSONWebToken):
    permission_classes = [IsAuthenticated]


class CoreVerifyJSONWebToken(VerifyJSONWebToken):
    permission_classes = [IsAuthenticated]


# 设置jwt 权限
obtain_jwt_token = ObtainJSONWebToken.as_view()
refresh_jwt_token = RefreshJSONWebToken.as_view()
verify_jwt_token = VerifyJSONWebToken.as_view()


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None

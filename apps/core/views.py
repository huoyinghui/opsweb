from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from .models import Boss
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


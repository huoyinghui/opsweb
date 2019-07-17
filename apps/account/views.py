from django.contrib.auth import get_user_model
from .serializers import UserSerializers
from .baseviews import BaseViewSet
from rest_framework.permissions import IsAuthenticated

User = get_user_model()
# Create your views here.


class UserViewSet(BaseViewSet):
    """
    用户增删改查
    """

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]
    search_fields = ['username']

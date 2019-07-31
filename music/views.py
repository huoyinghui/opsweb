from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from music.models import Music, Share
from music.serializers import MusicSerializer, ShareSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated, )


class ShareViewSet(viewsets.ModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    parser_classes = (JSONParser,)

    def get_permissions(self):
        """
        自定义方法权限:

        list: []
        create:
        :return: [IsAuthenticated]
        """
        if self.action in ('create',):
            self.permission_classes = [IsAuthenticated]
        elif self.action in ('list', ):
            self.permission_classes = []
        return [permission() for permission in self.permission_classes]

    # [GET] api/shares/
    def list(self, request, **kwargs):
        users = Share.objects.all()
        serializer = ShareSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # [POST] api/shares/
    def create(self, request, **kwargs):
        name = request.data.get('name')
        users = Share.objects.create(name=name)
        serializer = ShareSerializer(users)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
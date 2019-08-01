from music.serializers import MusicSerializer, ShareSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from music.models import Music, Share


from django.views import View


class MyBaseView(object):
    def dispatch(self, request, *args, **kwargs):
        print('bf view: {}'.format(request))
        ret = super(MyBaseView, self).dispatch(request, *args, **kwargs)
        print('af view: {}'.format(request))
        return ret


class MyView(MyBaseView, View):
    def get(self, request, *args, **kwargs):
        return Response('Get')


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)


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
        else:
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


#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:
Email:

date:
desc:

"""
import logging
from rest_framework import serializers
from opsweb.serializers import BaseAuthSerializer
from apps.core.models import Boss, User, PageJson

from rest_framework.serializers import ModelSerializer
from mptt.templatetags.mptt_tags import cache_tree_children


logger = logging.getLogger('debug')


class BossSerializers(ModelSerializer):
    """
    Boss序列化类
    """

    class Meta:
        model = Boss
        fields = '__all__'


class UserSerializers(ModelSerializer):
    """
    User序列化类
    """

    class Meta:
        model = User
        fields = ['id', 'nick_name', 'birthday', 'moblile']


class LoginSerializer(BaseAuthSerializer):
    username = serializers.CharField(required=True, max_length=30, write_only=True, help_text=u'用户名')
    password = serializers.CharField(required=True, write_only=True, help_text=u'密码')

    def validate(self, attrs):
        logger.debug(attrs)
        return attrs

    def to_representation(self, data=None):
        ret = super(LoginSerializer, self).to_representation(data)
        ret['token'] = data['token']
        ret['id'] = data['user'].get_uid
        ret['errcode'] = 0
        ret['errmsg'] = 'ok'
        logger.debug('LoginSerializer to_representation ok')
        return ret


class PageJsonSerializers(ModelSerializer):
    """
    PageJson序列化类
    """

    class Meta:
        model = PageJson
        fields = ['id', 'name', 'level', 'parent_id']


class RecursiveField(ModelSerializer):
    # 这个类代码保持不变
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class PageJsoTreeSerializer(PageJsonSerializers):
    # replies 是自引用的外键字段
    replies = RecursiveField(many=True)


def recursive_node_to_dict(node):
    """
    递归获取节点
    :param node:
    :return:
    """
    result = {
        'id': node.pk,
        'name': node.name,
        'level': node.level,
    }
    children = [recursive_node_to_dict(c) for c in node.get_children()]
    if children:
        result['children'] = children
    return result


def get_page_json_tree(queryset=None):
    """

    :param queryset:
    :return:
    """
    root_nodes = cache_tree_children(queryset)
    nodes = []
    for n in root_nodes:
        nodes.append(recursive_node_to_dict(n))
    return nodes


def main():
    import json
    nodes = get_page_json_tree()
    print(json.dumps(nodes, indent=4))
    pass


if __name__ == '__main__':
    main()

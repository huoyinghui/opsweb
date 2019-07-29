#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: 
Email:

date: 
desc:

"""

from .models import Boss, User, PageJson

from rest_framework.serializers import ModelSerializer
from mptt.templatetags.mptt_tags import cache_tree_children


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


class PageJsonSerializers(ModelSerializer):
    """
    PageJson序列化类
    """

    class Meta:
        model = PageJson
        fields = ['id', 'name', 'level', 'parent_id']


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


def get_page_json_tree():
    """

    :return:
    """
    root_nodes = cache_tree_children(PageJson.objects.all())
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

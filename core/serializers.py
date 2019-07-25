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


def main():
    pass


if __name__ == '__main__':
    main()

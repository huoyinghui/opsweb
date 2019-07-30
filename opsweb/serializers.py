#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: 
Email:

date: 
desc:

"""

# coding=utf-8

from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from . import errors
from .exceptions import MyException


class BaseSerializer(Serializer):
    """
    serializer base
    """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    errcode = serializers.IntegerField(read_only=True, default='0', help_text=u'错误码')
    errmsg = serializers.CharField(read_only=True, default='', help_text=u'详细信息')

    def to_representation(self, instance=None):
        return {'errcode': 0, 'errmsg': 'ok'}


class BaseAuthSerializer(JSONWebTokenSerializer):
    """
    serializer base JSONWebTokenSerializer
    """
    errcode = serializers.IntegerField(read_only=True, default='0', help_text=u'错误码')
    errmsg = serializers.CharField(read_only=True, default='', help_text=u'详细信息')

    def to_representation(self, instance=None):
        return {'errcode': 0, 'errmsg': 'ok'}


class TokenRequest(Serializer):
    """
    serializer used for verifying code.
    """
    username = serializers.CharField(write_only=True, help_text=u'用户名')
    password = serializers.CharField(write_only=True, help_text=u'密码')

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise MyException(_('username or passwrod is error'), errors.AUTH_USERNAME_OR_PASSWORD_ERROR)
        return attrs


class TokenSerializer(Serializer):
    """
    serializer used for verifying code.
    """
    token = serializers.CharField(read_only=True)


class AuthSerializer(BaseAuthSerializer):
    """
    serializer used for verifying code.
    """
    username = serializers.CharField(write_only=True, help_text=u'用户名')
    password = serializers.CharField(write_only=True, help_text=u'密码')
    token = serializers.CharField(read_only=True, help_text=u'token')
    role = serializers.CharField(read_only=True, help_text=u'角色')
    full_name = serializers.CharField(read_only=True, help_text=u'全名')

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise MyException(_('username or passwrod is error'), errors.Auth.AUTH_ERROR)
        return attrs

    def to_representation(self, data=None):
        ret = super(AuthSerializer, self).to_representation(data)
        ret['token'] = data['token']
        ret['role'] = data['role']
        ret['full_name'] = data['full_name']
        return ret


class BaseModelSerializer(ModelSerializer):
    """
    serializer base
    """
    errcode = serializers.IntegerField(read_only=True, default='0', help_text=u'错误码')
    errmsg = serializers.CharField(read_only=True, default='', help_text=u'详细信息')

    def to_representation(self, instance=None):
        ret = super(BaseModelSerializer, self).to_representation(instance)
        ret['errcode'] = 0
        ret['errmsg'] = 'ok'
        return ret


class BaseListSerializer(Serializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def to_representation(self, data):
        ret = {'errcode': 0, 'errmsg': 'ok',
               'data': self.fields['data'].child.__class__(data, many=True, context=self.context).data}
        return ret


def main():
    pass


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author:Eric
from .models import User
from rest_framework.serializers import ModelSerializer


class UserSerializers(ModelSerializer):
    """
    用户序列化类
    """

    class Meta:
        model = User
        fields = '__all__'
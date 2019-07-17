#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: 
Email:

date: 
desc:

"""

from .models import Boss
from rest_framework.serializers import ModelSerializer


class BossSerializers(ModelSerializer):
    """
    Boss序列化类
    """

    class Meta:
        model = Boss
        fields = '__all__'


def main():
    pass


if __name__ == '__main__':
    main()

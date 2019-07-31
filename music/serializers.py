#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: 
Email:

date: 
desc:

"""
from django.utils.timezone import now
from rest_framework import serializers
from .models import Music


class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return value.upper()


class MusicSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    # singer 字段自定处理
    singer = ToUpperCaseCharField()

    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date',
                  'created', 'days_since_created')

    @staticmethod
    def get_days_since_created(obj):
        return (now() - obj.created).days


def main():
    pass


if __name__ == '__main__':
    main()

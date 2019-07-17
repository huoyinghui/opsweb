#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import django_filters

from django_filters.rest_framework import FilterSet
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFilters(FilterSet):
    """
    用户搜索过滤器
    """
    username = django_filters.CharFilter(name='username', lookup_expr='icontains')

    class Meta:
        model = User
        fileds = ['username']
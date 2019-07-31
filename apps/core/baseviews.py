#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

# Create your views here.


class BaseViewSet(ModelViewSet):

    queryset = None
    serializer_class = None
    permission_classes = []
    # # 分页
    # pagination_class = []
    # 搜索
    filter_backends = [filters.SearchFilter]
    search_fields = []

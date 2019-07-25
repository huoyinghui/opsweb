#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from .views import UserSet, PageJsonSet

# register的可选参数 base_name: 用来生成urls名字，如果viewset中没有包含queryset, base_name一定要有
core_router = DefaultRouter()
# core_router.register(r'core', ListUser, base_name='core')
core_router.register(r'core/user', UserSet, base_name='core_user')
core_router.register(r'core/tree', PageJsonSet, base_name='core_tree')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: 
Email:

date: 
desc:

"""
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException, ErrorDetail
from rest_framework.views import exception_handler

from . import errors


class MyException(APIException):
    """
    Base class for REST framework exceptions.
    Subclasses should provide `.status_code` and `.default_detail` properties.
    """
    status_code = status.HTTP_400_BAD_REQUEST
    # status_code = status.HTTP_200_OK
    default_err_msg = _('A request error occurred.')
    default_err_code = 55555

    def __init__(self, detail=None, error_code=None):
        if detail is not None:
            self.detail = force_text(detail)
        else:
            self.detail = force_text(self.default_detail)
        if error_code is not None:
            self.error_code = int(force_text(error_code))
        else:
            self.error_code = force_text(self.default_error_code)

    def __str__(self):
        return self.err_msg


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            # print exc.detail
            error_code = getattr(exc, 'error_code', None)
            if error_code:
                response.data['errcode'] = int(exc.error_code)
                response.data['errmsg'] = exc.detail
                response.data.pop('detail', None)
            else:
                commen_error_handler(exc, response)
            # response.data['errmsg'] =
            # response.data.pop('detail', None)
            response.status_code = status.HTTP_200_OK
        elif response.status_code == status.HTTP_401_UNAUTHORIZED:
            response.data['errcode'] = int(errors.Account.UNAUTHORIZED)
            response.data['errmsg'] = _('unauthorized')
            if 'detail' in response.data:
                response.data.pop('detail', None)
            response.status_code = status.HTTP_200_OK
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            response.data['errcode'] = errors.System.NOT_FOUND
            response.data['errmsg'] = exc.message
            if 'detail' in response.data:
                response.data.pop('detail', None)
            response.status_code = status.HTTP_200_OK
        else:
            commen_error_handler(exc, response)
            response.status_code = status.HTTP_200_OK
    else:
        print('22222222222>>>>>>>>>>>>>')

    return response


def commen_error_handler(exc, response):
    if isinstance(exc.detail, dict):
        request_error_handler(exc, response)
    elif isinstance(exc.detail, ErrorDetail):
        response.data['errmsg'] = exc.detail
        response.data['errcode'] = errors.System.ERROR_DETAIL
        response.data.pop('detail', None)
    else:
        system_error_handler(response)


def system_error_handler(response):
    response.data['errmsg'] = 'system error'
    response.data['errcode'] = errors.System.ERROR


def request_error_handler(exc, response):
    response.data['errcode'] = int(5555)
    for k, v in exc.detail.items():
        if k == 'errcode':
            continue
        # print k, v
        response.data['errmsg'] = '%s:%s' % (k, ','.join(v))
        response.data.pop(k, None)


def main():
    pass


if __name__ == '__main__':
    main()

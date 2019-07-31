from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 150

    def get_paginated_response(self, data):
        data['count'] = self.page.paginator.count
        data['next'] = self.get_next_link()
        data['previous'] = self.get_previous_link()
        return Response(data)


class CommentPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'count'
    max_page_size = 100

    def get_paginated_response(self, data):
        data['total'] = self.page.paginator.count
        data['next'] = self.get_next_link()
        data['previous'] = self.get_previous_link()
        return Response(data)


class ContentsListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 150

    def get_paginated_response(self, data):
        data['count'] = self.page.paginator.count
        data['next'] = self.get_next_link()
        data['previous'] = self.get_previous_link()
        return Response(data)
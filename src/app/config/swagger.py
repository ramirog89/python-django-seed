from drf_yasg.inspectors import PaginatorInspector
from drf_yasg import openapi
from collections import OrderedDict


class CustomPaginatorClass(PaginatorInspector):

    def get_paginated_response(self, paginator, response_schema):
        return openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=OrderedDict((
                ('total', openapi.Schema(type=openapi.TYPE_INTEGER)),
                ('items', response_schema),
            )),
            required=['items']
        )

    def get_paginator_parameters(self, paginator):
        return [
            openapi.Parameter('page', openapi.IN_QUERY, "Page Number", False, None, openapi.TYPE_INTEGER),
            openapi.Parameter('page_size', openapi.IN_QUERY, "Page Size", False, None, openapi.TYPE_INTEGER)
        ]

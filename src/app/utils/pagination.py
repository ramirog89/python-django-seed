from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from src.app.dtos.pagination import PaginationDto


class PaginationObject(object):
    pass


class CustomPagination(PageNumberPagination, LimitOffsetPagination):
    page_size = 5
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = PaginationObject()
        response.total = self.page.paginator.count
        response.items = data
        return PaginationDto(response).data


def paginate(list, request, dtoType):
    paginator = CustomPagination()
    result_page = paginator.paginate_queryset(list, request)
    dtos = dtoType(result_page, many=True)
    return paginator.get_paginated_response(dtos.data)
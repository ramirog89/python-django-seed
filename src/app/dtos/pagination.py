from rest_framework import serializers, pagination
from src.app.dtos.user import UserDto


class PaginationQueryParamsDto(serializers.Serializer):
    page = serializers.IntegerField(required=False)
    page_size = serializers.IntegerField(required=False)


class PaginationDto(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'total': instance.total,
            'items': instance.items
        }

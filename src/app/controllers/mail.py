from serum import inject
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from src.app.services.mail import MailService


@swagger_auto_schema(method='POST', responses={200: None})
@api_view(['POST'])
@permission_classes([AllowAny])
@inject
def send(request, service: MailService):
    try:
        service.sendMail()
        return Response(status=status.HTTP_200_OK)
    except Exception as error:
        return Response(None, status=status.HTTP_400_BAD_REQUEST)
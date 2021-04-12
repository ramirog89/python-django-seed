from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from src.app.tasks.mail import sendEmail


@swagger_auto_schema(method='POST', responses={200: None})
@api_view(['POST'])
def send(request):
    try:
        sendEmail.delay()
        return Response(status=status.HTTP_200_OK)
    except Exception as error:
        print(error)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)
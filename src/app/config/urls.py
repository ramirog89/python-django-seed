# django url handler
from django.urls import path
# rest api features
from rest_framework import routers, permissions

# swagger views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# api controllers
from src.app import controllers

# schema for swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Rest API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url="http://localhost:8000/",
    urlconf="src.app.config.urls"
)


router = routers.DefaultRouter()


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('auth/login', controllers.authentication.login, name='auth user'),
    path('auth/logout', controllers.authentication.logout, name='logout user'),
    path('users', controllers.user.list, name='get user list'),
    path('users/<int:id>', controllers.user.get, name='get user'),
    path('users/create', controllers.user.create, name='create user'),
    path('users/update/<int:id>', controllers.user.update, name='update user'),
    path('users/delete/<int:id>', controllers.user.delete, name='delete user')
]

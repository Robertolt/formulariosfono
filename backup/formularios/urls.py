"""formularios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from formularios.base.views import home, resposta_questionario_view, sucesso

# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
# 
# 
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     # Serializers define the API representation.
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']
# 
# 
# class UserViewSet(viewsets.ModelViewSet):
#     # ViewSets define the view behavior.
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# 
# 
# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', FormRespostaView.as_view(), name='home'),
    path('', home, name='home'),
    path('sucesso', sucesso, name='sucesso'),
    path('resposta_questionario/<int:pk>', resposta_questionario_view, name='resposta-questionario-view'),
    path('api-auth/', include('rest_framework.urls'))
]

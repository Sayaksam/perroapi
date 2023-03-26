from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from core.models import User as user_models
from django.http import HttpResponse

from user.serializers import UserSerialzer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):

    serializer_class = UserSerialzer


class CreateTokenView(ObtainAuthToken):

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


def getuser(self, uname):
    pwd = user_models.objects.filter(email=uname).values("password")
    return HttpResponse(list(pwd)[0]["password"])


class ManageUserView(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerialzer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):

        return self.request.user

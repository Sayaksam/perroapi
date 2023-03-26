from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from core.models import User as user_models
from django.db.models import Subquery, OuterRef
from rest_framework import generics, authentication, permissions
from user.serializers import UserSerialzer, AuthTokenSerializer
from rest_framework.views import APIView


def justatest(request):

    return HttpResponse("Welcome to Perroworld!!!! Test Successful :) ")


@api_view(["GET"])
def my_testing_user(request):
    userid = list(
        Token.objects.filter(
            key=request.headers["Authorization"].split(" ")[1]
        ).values_list("user_id", flat=True)
    )[0]
    request.user = user_models.objects.get(id=userid)
    return Response(data={"name": request.user.location})


class MyUserView(APIView):

    # serializer_class = UserSerialzer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        details = {
            "name": self.request.user.name,
            "location": self.request.user.location,
            "email": self.request.user.email,
            "id": self.request.user.id,
        }

        return Response({"data": details})


class checkToken(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        token_number = Token.objects.filter(user_id=self.request.user.id).values(
            "key", "user_id"
        )

        return Response(data={"token": list(token_number)[0]})
